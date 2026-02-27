# books-for-indigo

Books I've read to Indigo, hosted at [readingstori.es](https://readingstori.es).

This is an incomplete list. The page works fully without JavaScript — JS is optional and used only to update stats meters from live data.

**Conventions:**
- ⭐ = starred favourites, `(currently reading)` = in progress.
- **Credits:** Solo author-illustrators get plain `by Name`. Collaborations get explicit role labels: `by Name (Author), Name (Illustrator)`.
- **Dates:** First publication year. For translations: `(YEAR, English translation YEAR)`.

## Suggest a book

Got a recommendation? [Open an issue](https://github.com/oatsandsugar/books-for-indigo/issues/new)!

## Webring

Looking for other nerdy parents who maintain personal sites or book lists — would love to start a webring. If that's you, [open an issue](https://github.com/oatsandsugar/books-for-indigo/issues/new?title=Webring%20-%20let%27s%20link%20up!&labels=webring&body=My%20homepage%3A%20)!

## Extracting data

The HTML is structured for easy scraping with `querySelectorAll`:

```js
// All books
document.querySelectorAll('li[data-status]')

// Starred favourites
document.querySelectorAll('li[data-starred]')

// Currently reading
document.querySelectorAll('li[data-status="reading"]')

// Books from a specific year
document.querySelectorAll('li[data-year="2023"]')

// Books from a decade (starts-with match)
document.querySelectorAll('li[data-year^="199"]') // 1990s

// All titles
document.querySelectorAll('cite')

// All authors/contributors
document.querySelectorAll('.author')

// Roles (Author, Illustrator, Compiler, etc.)
document.querySelectorAll('.role')

// Caldecott Medal winners
document.querySelectorAll('li[data-caldecott-medal]')

// Caldecott Honor books
document.querySelectorAll('li[data-caldecott-honor]')

// NYT Best Illustrated
document.querySelectorAll('li[data-nyt-illustrated]')

// Any Caldecott (medal or honor)
document.querySelectorAll('li[data-caldecott-medal], li[data-caldecott-honor]')

// Titles of all Caldecott honorees from the 1990s
[...document.querySelectorAll('li[data-caldecott-honor][data-year^="199"]')]
  .map(li => li.querySelector('cite').textContent)

// Caldecott Medal years you've read
[...document.querySelectorAll('li[data-caldecott-medal]')]
  .map(li => li.dataset.caldecottMedal).sort()

// Caldecott Medal years you're missing
const read = new Set([...document.querySelectorAll('li[data-caldecott-medal]')]
  .map(li => li.dataset.caldecottMedal));
Array.from({length: 2026-1938+1}, (_, i) => String(1938+i))
  .filter(y => !read.has(y))

// Decade with the most starred books
Object.entries(
  [...document.querySelectorAll('li[data-starred]')]
    .reduce((acc, li) => {
      const d = Math.floor(li.dataset.year / 10) * 10 + 's';
      acc[d] = (acc[d] || 0) + 1;
      return acc;
    }, {})
).sort((a, b) => b[1] - a[1])[0]
```

## Formerly Featured Quotes

- "Books are a uniquely portable magic." — Stephen King, *On Writing: A Memoir of the Craft* (2000)
