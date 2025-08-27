import { QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"
import { JSX } from "preact"
import style from "./styles/contentMeta.scss"

interface AuthorLinksOptions {
  showComma: boolean
}

const defaultOptions: AuthorLinksOptions = {
  showComma: true,
}

export default ((opts?: Partial<AuthorLinksOptions>) => {
  // Merge options with defaults
  const options: AuthorLinksOptions = { ...defaultOptions, ...opts }

  function AuthorLinks({ fileData, displayClass }: QuartzComponentProps) {
    const authors = fileData.frontmatter?.authors
    console.log("AuthorLinks received:", { 
      authors,
      type: authors ? typeof authors : null,
      isArray: Array.isArray(authors),
      content: authors
    })

    if (authors) {
      // Parse authors - can be string or array
      let authorLinks: JSX.Element[] = []
      
      // Function to process a single author string
      const processAuthorString = (authorStr: string) => {
        console.log("Processing author string:", authorStr)
        
        // Handle strings that already contain wikilinks
        if (authorStr.includes("[[")) {
          const regex = /\[\[(.*?)(?:\|.*?)?\]\]/g
          let match
          
          while ((match = regex.exec(authorStr)) !== null) {
            const authorName = match[1]
            console.log("Found author with wikilink:", authorName)
            
            // Create link with the same classes that Quartz uses for internal links
            authorLinks.push(
              <a href={`/${authorName}`} class="internal" data-slug={authorName}>
                {authorName}
              </a>
            )
          }
        } else {
          // Handle plain text authors without wikilinks
          console.log("Found plain author name:", authorStr)
          authorLinks.push(
            <a href={`/${authorStr}`} class="internal" data-slug={authorStr}>
              {authorStr}
            </a>
          )
        }
      }
      
      if (typeof authors === 'string') {
        // Handle string format
        console.log("Processing string format")
        processAuthorString(authors)
      } else if (Array.isArray(authors)) {
        // Handle array format
        console.log("Processing array format with length:", authors.length)
        authors.forEach((author, index) => {
          console.log(`Array item ${index}:`, author, typeof author)
          if (typeof author === 'string') {
            processAuthorString(author)
          }
        })
      }

      console.log("Generated author links:", authorLinks.length)
      if (authorLinks.length > 0) {
        // Just return the author links directly without wrapping in another p tag
        // since the ContentMeta component will handle the wrapping
        return (
          <>
            {authorLinks}
          </>
        )
      } else {
        console.log("No author links were generated")
      }
    }
    
    return null
  }

  AuthorLinks.css = style

  return AuthorLinks
}) satisfies QuartzComponentConstructor