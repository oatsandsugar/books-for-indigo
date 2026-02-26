# books-for-indigo

Books I've read to Indigo, hosted at [readingstori.es](https://readingstori.es).

This is an incomplete list.

**Conventions:** ⭐ = starred favourites, `(currently reading)` = in progress.

## Suggest a book

Got a recommendation? [Open an issue](https://github.com/oatsandsugar/books-for-indigo/issues/new)!

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
```
