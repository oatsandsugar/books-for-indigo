# books-for-indigo

Books I've read to Indigo, hosted at [readingstori.es](https://readingstori.es).

This is an incomplete list. The reading list remains usable without JavaScript; filtering, sorting, and the personal completion checklist are client-side enhancements.

The completion checklist is off by default; the "track your reading" toggle above the list turns it on. Completion state is stored only in the visitor's browser with `localStorage`. It is not sent anywhere or synced between devices.

**RSS feeds:** [All books](https://readingstori.es/feed.xml) · [Starred only](https://readingstori.es/starred.xml)

**Conventions:**
- ⭐ = starred favourites, `(currently reading)` = in progress.
- **Credits:** Solo author-illustrators get plain `by Name`. Collaborations get explicit role labels: `by Name (Author), Name (Illustrator)`.
- **Dates:** First publication year. For translations: `(YEAR, English translation YEAR)`.
- **Publishers:** Use a consistent name for the original publisher or imprint. Check existing values before adding another spelling. Keep distinct imprints, regional operations, and historical publishers separate; shared corporate ownership is not a reason to combine them.

### Publisher name normalization

Publisher analytics use `data-edition-publisher` when present, otherwise `data-publisher`, and combine exact publisher/imprint names. Use these canonical names for equivalent labels:

| Canonical name | Equivalent labels |
|---|---|
| G. P. Putnam's Sons | G.P. Putnam's Sons |
| DK | Dorling Kindersley |
| Owlkids Books | Owlkids |
| Knopf Books for Young Readers | Alfred A. Knopf Books for Young Readers |
| Dial Books | Dial Books for Young Readers |
| Henry Holt and Company | Henry Holt |
| Peachtree Publishers | Peachtree Publishing |
| Doubleday | Doubleday & Company |

Verified against publisher sources: [DK](https://dk.com/en-us/pages/permissions), [Owlkids](https://owlkidsbooks.com/about-us/), [Knopf](https://www.penguinrandomhouse.com/books/219129/the-noisy-paint-box-the-colors-and-sounds-of-kandinskys-abstract-art-by-barb-rosenstock-illustrated-by-mary-grandpre/), [Dial](https://www.penguin.com/dial-overview/), [Henry Holt](https://us.macmillan.com/books/9781466822344/ifyouspentadaywiththoreauatwaldenpond/), [Peachtree](https://www.peachtreebooks.com/wp-content/uploads/2021/06/PT-Internship-Posting-Summer-2025.pdf), and [Doubleday](https://www.randomhouse.com/doubleday/history.html). The Putnam change only standardizes spacing.

The four existing `Alfred A. Knopf` entries were individually checked and assigned to Knopf Books for Young Readers: [Song and Dance Man](https://www.penguinrandomhouse.com/books/465/song-and-dance-man-by-karen-ackerman-illustrated-by-stephen-gammell/), [All Are Welcome](https://assets.penguinrandomhouse.com/book-resumes/PenfoldAlexandra_ALL%20ARE%20WELCOME.pdf), [Let's Make Music](https://www.penguinrandomhouse.com/books/678250/lets-make-music-an-all-are-welcome-board-book-by-alexandra-penfold-illustrated-by-suzanne-kaufman/), and [The Spice Box](https://penguinrandomhouseelementaryeducation.com/book/?isbn=9780593427156). Do not treat the adult Knopf imprint as an alias for the children's imprint.

The `Little, Brown and Company` entry for [Fred Gets Dressed](https://www.littlebrownlibrary.com/titles/peter-brown-2/fred-gets-dressed/9780316200646/) was also assigned to its verified imprint, Little, Brown Books for Young Readers. This is a book-specific correction, not an alias between the adult and children’s divisions.

This is name normalization, not an audit of every book's first edition. Ambiguous broader labels, such as Viking, Random House, or HarperCollins, need edition-specific evidence before assigning them to a particular imprint. Preserve Harper & Row, Houghton Mifflin, and other historical publishers rather than assigning their books to later owners.

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

### Edition publishers

`data-publisher` retains the original publisher. Optional `data-edition-publisher` records the publisher or imprint of the edition read. Publisher analytics use the edition value when present, otherwise the original publisher. There is one imprint-level chart, with no parent-company grouping or edition/original view toggle.

Populate edition overrides from the reader’s instructions or evidence about their copy, and record that evidence in `data/edition-publishers.json`. A catalogue entry for a matching title alone is insufficient. Missing edition information does not remove a book from publisher comparisons when an original publisher is known. The chart shows the top 12 publishers with at least three books. Buttons rank by total books or starred books; clicking a publisher opens its book list.

Both publisher attributes are bibliographic metadata, not awards. Existing original-publication years and country fields do not change when recording an edition publisher.
