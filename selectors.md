# Selectors reference

The book list in [`index.html`](index.html) is structured for scraping with `querySelectorAll`. Run these in the browser console on [readingstori.es](https://readingstori.es/).

## Book attributes

Each book is an `<li>` with:

| Attribute | Meaning |
| --- | --- |
| `data-year` | First publication year; `unknown` when unconfirmed (or best-guess for ancient texts, e.g. `-500`) |
| `data-status` | `"read"` or `"reading"` |
| `data-starred` | Boolean; favourites (shown as ⭐) |
| `data-added` | Date added to the list (`YYYY-MM-DD`) |
| `data-country` | ISO country code for the work's origin |
| `data-publisher` | Original publisher |
| `data-recommended` | Boolean; recommended via a GitHub issue |
| `data-review` | Short review text (when present) |

Award attributes (value = award year unless noted):

| Attribute | Award |
| --- | --- |
| `data-caldecott-medal` | Caldecott Medal |
| `data-caldecott-honor` | Caldecott Honor |
| `data-nyt-illustrated` | NYT Best Illustrated |
| `data-newbery-medal` | Newbery Medal |
| `data-newbery-honor` | Newbery Honor |
| `data-greenaway-medal` | Kate Greenaway Medal |
| `data-cbca-picture-book` | CBCA Picture Book of the Year |
| `data-cbca-picture-book-highly-commended` | CBCA Picture Book Highly Commended / Honour |
| `data-cbca-picture-book-shortlist` | CBCA Picture Book shortlist |
| `data-cbca-early-childhood-shortlist` | CBCA Early Childhood shortlist |
| `data-cbca-notable` | CBCA Notable |

Awarded titles often also have a `title` tooltip on `<cite>` with human-readable award text.

Inside each `<li>`:

- `<cite>` — title
- `<span class="author">` — author/contributor
- `<span class="role">` — role label (Author, Illustrator, Compiler, Editor, etc.)

Sections use `ul[data-section]` with values `picture`, `chapter`, or `poetry`.

## Selectors

```js
// All books
document.querySelectorAll('li[data-status]')

// Starred favourites
document.querySelectorAll('li[data-starred]')

// Currently reading
document.querySelectorAll('li[data-status="reading"]')

// Community recommendations
document.querySelectorAll('li[data-recommended]')

// Books with a written review
document.querySelectorAll('li[data-review]')

// Books from a specific year
document.querySelectorAll('li[data-year="2023"]')

// Books from a decade (starts-with match)
document.querySelectorAll('li[data-year^="199"]') // 1990s

// By country or publisher
document.querySelectorAll('li[data-country="AU"]')
document.querySelectorAll('li[data-publisher="Candlewick Press"]')

// Recently added (exact date)
document.querySelectorAll('li[data-added="2026-08-11"]')

// All titles / authors / roles
document.querySelectorAll('cite')
document.querySelectorAll('.author')
document.querySelectorAll('.role')

// Awards
document.querySelectorAll('li[data-caldecott-medal]')
document.querySelectorAll('li[data-caldecott-honor]')
document.querySelectorAll('li[data-nyt-illustrated]')
document.querySelectorAll('li[data-newbery-medal], li[data-newbery-honor]')
document.querySelectorAll('li[data-greenaway-medal]')
document.querySelectorAll('li[data-cbca-picture-book], li[data-cbca-notable]')
document.querySelectorAll('li[data-cbca-picture-book-highly-commended], li[data-cbca-picture-book-shortlist], li[data-cbca-early-childhood-shortlist]')

// Any Caldecott (medal or honor)
document.querySelectorAll('li[data-caldecott-medal], li[data-caldecott-honor]')

// Section lists
document.querySelectorAll('ul[data-section="picture"] li[data-status]')
```

## Snippets

```js
// Titles of all Caldecott honorees from the 1990s
[...document.querySelectorAll('li[data-caldecott-honor][data-year^="199"]')]
  .map(li => li.querySelector('cite').textContent);

// Caldecott Medal years you've read
[...document.querySelectorAll('li[data-caldecott-medal]')]
  .map(li => li.dataset.caldecottMedal).sort();

// Caldecott Medal years you're missing
const read = new Set([...document.querySelectorAll('li[data-caldecott-medal]')]
  .map(li => li.dataset.caldecottMedal));
Array.from({length: 2026-1938+1}, (_, i) => String(1938+i))
  .filter(y => !read.has(y));

// Decade with the most starred books
Object.entries(
  [...document.querySelectorAll('li[data-starred]')]
    .reduce((acc, li) => {
      const d = Math.floor(li.dataset.year / 10) * 10 + 's';
      acc[d] = (acc[d] || 0) + 1;
      return acc;
    }, {})
).sort((a, b) => b[1] - a[1])[0];

// Starred books with no award attrs in our HTML (not the same as "won no awards";
// tagging is incomplete, including for awards we do capture like CBCA)
const NON_AWARD = new Set([
  'data-year', 'data-status', 'data-starred', 'data-review',
  'data-recommended', 'data-added', 'data-country', 'data-publisher'
]);
[...document.querySelectorAll('li[data-starred]')]
  .filter(li => ![...li.attributes].some(a =>
    a.name.startsWith('data-') && !NON_AWARD.has(a.name)
  ))
  .map(li => li.querySelector('cite').textContent);

// Export a simple CSV of title, year, country
[...document.querySelectorAll('li[data-status]')]
  .map(li => [
    JSON.stringify(li.querySelector('cite')?.textContent ?? ''),
    li.dataset.year,
    li.dataset.country ?? ''
  ].join(','))
  .join('\n');
```
