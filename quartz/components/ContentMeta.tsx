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
  showReadingTime: false,
  showAuthors: true,
  showComma: true,
}

export default ((opts?: Partial<ContentMetaOptions>) => {
  // Merge options with defaults
  const options: ContentMetaOptions = { ...defaultOptions, ...opts }
  
  // Initialize the AuthorLinks component
  const authorLinksComponent = AuthorLinks({ showComma: options.showComma })

  function ContentMetadata({ cfg, fileData, displayClass, ...rest }: QuartzComponentProps) {
    const segments: (string | JSX.Element)[] = []

    // Display date and reading time
    const dateAndReadingTime: (string | JSX.Element)[] = []

    if (fileData.dates) {
      dateAndReadingTime.push(<Date date={getDate(cfg, fileData)!} locale={cfg.locale} />)
    }

    // Display reading time if enabled and text is available
    if (options.showReadingTime && fileData.text) {
      const { minutes, words: _words } = readingTime(fileData.text)
      const displayedTime = i18n(cfg.locale).components.contentMeta.readingTime({
        minutes: Math.ceil(minutes),
      })
      dateAndReadingTime.push(<span>{displayedTime}</span>)
    }

    // First put authors if available (this ensures they appear first)
    if (options.showAuthors && fileData.frontmatter?.authors) {
      const authorLinks = authorLinksComponent({ cfg, fileData, displayClass, ...rest })
      if (authorLinks) {
        // Add authors section as the first item
        segments.push(
          <p show-comma={options.showComma} class={classNames(displayClass, "content-meta", "author-meta")}>
            <span class="authors">
              {authorLinks}
            </span>
          </p>
        )
      }
    }

    // Then add date and reading time in their own segment
    if (dateAndReadingTime.length > 0) {
      segments.push(
        <p show-comma={options.showComma} class={classNames(displayClass, "content-meta")}>
          {dateAndReadingTime}
        </p>
      )
    }

    // Filter out any null segments
    const filteredSegments = segments.filter(Boolean)

    if (filteredSegments.length > 0) {
      return <>{filteredSegments}</>
    }
    
    return null
  }

  // Add some additional CSS for spacing between author and date sections
  ContentMetadata.css = style + `
  .author-meta {
    margin-bottom: 0.25rem;
  }
  `

  return ContentMetadata
}) satisfies QuartzComponentConstructor
