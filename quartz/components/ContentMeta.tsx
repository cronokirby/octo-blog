import { Date, getDate } from "./Date"
import { QuartzComponentConstructor, QuartzComponentProps } from "./types"
import readingTime from "reading-time"
import { classNames } from "../util/lang"
import { i18n } from "../i18n"
import { JSX } from "preact"
import style from "./styles/contentMeta.scss"
import AuthorLinks from "./AuthorLinks"

interface ContentMetaOptions {
  /**
   * Whether to display reading time
   */
  showReadingTime: boolean
  /**
   * Whether to display authors
   */
  showAuthors: boolean
  showComma: boolean
}

const defaultOptions: ContentMetaOptions = {
  showReadingTime: true,
  showAuthors: true,
  showComma: true,
}

export default ((opts?: Partial<ContentMetaOptions>) => {
  // Merge options with defaults
  const options: ContentMetaOptions = { ...defaultOptions, ...opts }
  
  // Initialize the AuthorLinks component
  const authorLinksComponent = AuthorLinks({ showComma: options.showComma })

  function ContentMetadata({ cfg, fileData, displayClass, ...rest }: QuartzComponentProps) {
    // Debug output to console
    console.log("ContentMeta fileData:", {
      slug: fileData.slug,
      frontmatter: fileData.frontmatter,
      hasAuthors: Boolean(fileData.frontmatter?.authors),
      authorType: fileData.frontmatter?.authors ? typeof fileData.frontmatter.authors : null,
      hasText: Boolean(fileData.text),
      hasDates: Boolean(fileData.dates)
    })
    
    const segments: (string | JSX.Element)[] = []

    // Display authors if enabled and available
    if (options.showAuthors && fileData.frontmatter?.authors) {
      const authorLinks = authorLinksComponent({ cfg, fileData, displayClass, ...rest })
      console.log("Author component result:", authorLinks)
      if (authorLinks) {
        // Add authors section
        segments.push(
          <span class="authors">
            {authorLinks}
          </span>
        )
      }
    }

    if (fileData.dates) {
      segments.push(<Date date={getDate(cfg, fileData)!} locale={cfg.locale} />)
    }

    // Display reading time if enabled and text is available
    if (options.showReadingTime && fileData.text) {
      const { minutes, words: _words } = readingTime(fileData.text)
      const displayedTime = i18n(cfg.locale).components.contentMeta.readingTime({
        minutes: Math.ceil(minutes),
      })
      segments.push(<span>{displayedTime}</span>)
    }

    // Filter out any null segments (like if AuthorLinks returned null)
    const filteredSegments = segments.filter(Boolean)
    console.log("Filtered segments:", filteredSegments.length)

    if (filteredSegments.length > 0) {
      return (
        <p show-comma={options.showComma} class={classNames(displayClass, "content-meta")}>
          {filteredSegments}
        </p>
      )
    }
    
    return null
  }

  ContentMetadata.css = style

  return ContentMetadata
}) satisfies QuartzComponentConstructor
