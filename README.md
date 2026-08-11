# books-for-indigo

Books I've read to Indigo, hosted at [readingstori.es](https://readingstori.es).

This is an incomplete list. The reading list remains usable without JavaScript; filtering, sorting, and the personal completion checklist are client-side enhancements.

The completion checklist is off by default; the "track your reading" toggle above the list turns it on. Completion state is stored only in the visitor's browser with `localStorage`. It is not sent anywhere or synced between devices.

**RSS feeds:** [All books](https://readingstori.es/feed.xml) · [Starred only](https://readingstori.es/starred.xml)

**Conventions:**
- ⭐ = starred favourites, `(currently reading)` = in progress.
- **Credits:** Solo author-illustrators get plain `by Name`. Collaborations get explicit role labels: `by Name (Author), Name (Illustrator)`.
- **Dates:** First publication year. For translations: `(YEAR, English translation YEAR)`.

## Suggest a book

Got a recommendation? [Open an issue](https://github.com/oatsandsugar/books-for-indigo/issues/new)!

## Webring

Part of the [90s Internet Webring](https://90s-internet.com) ([random](https://90s-internet.com/#random) · [join](https://github.com/oatsandsugar/90s-internet/issues/new?title=Join%20the%20webring&labels=join)). Especially glad to link up with other nerdy parents running personal sites or book lists. Got a book recommendation? [Open an issue](https://github.com/oatsandsugar/books-for-indigo/issues/new)!

## Extracting data

The HTML is structured for easy scraping with `querySelectorAll`. A couple of starters:

```js
// All books
document.querySelectorAll('li[data-status]')

// Starred favourites
document.querySelectorAll('li[data-starred]')
```

Full attribute list, award selectors, and more snippets: [selectors.md](selectors.md).

## Formerly Featured Quotes

- "Books are a uniquely portable magic." — Stephen King, *On Writing: A Memoir of the Craft* (2000)
