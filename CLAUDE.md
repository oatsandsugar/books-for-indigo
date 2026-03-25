# CLAUDE.md

## Project

Static book list hosted at readingstori.es via GitHub Pages (main branch, root).
Repo: github.com/oatsandsugar/books-for-indigo

## Files

- `index.html` — the book list. Bare HTML, minimal CSS (monospace font, dark mode), no JS. Old-internet aesthetic.
- `caldecott.html` — Caldecott Medal checklist page.
- `cbca.html` — CBCA (Children's Book Council of Australia) checklist page.
- `greenaway.html` — Kate Greenaway Medal checklist page.
- `feed.xml` — RSS feed of all recently added books. Updated manually when books are added.
- `starred.xml` — RSS feed of starred (⭐) books only. Updated manually when starred books are added.
- `sitemap.xml` — Human-readable sitemap.
- `README.md` — project meta, conventions, querySelectorAll extraction docs, formerly featured quotes.
- `CNAME` — custom domain (`readingstori.es`).
- `LICENSE` — MIT License.

## HTML structure

Each book is a `<li>` with:
- `data-year` — publication year (or best-guess for ancient texts, e.g. `-500` for Tao Te Ching)
- `data-starred` — boolean attribute for favourites (displayed as ⭐ at start of line)
- `data-status` — `"read"` or `"reading"`
- `<cite>` — book title. If awarded, has `title` attribute with award info (hover tooltip).
- `<span class="author">` — each author/contributor
- `<span class="role">` — role label (Author, Illustrator, Compiler, Editor, etc.)
- `data-caldecott-medal` — Caldecott Medal year (value = award year)
- `data-caldecott-honor` — Caldecott Honor year (value = award year)
- `data-nyt-illustrated` — NYT Best Illustrated year (value = award year)
- `data-recommended` — boolean attribute for community-recommended books (from GitHub issues)
- `data-added` — date the book was added to the list (YYYY-MM-DD, approximate — based on commit date). JS shows a "NEW" badge for books added within the last 2 weeks.

Currently-reading books are marked with `(currently reading)` prefix text.

## Conventions

- Minimal CSS, tiny JS for the "NEW" badge only. Page works without JS.
- When adding a book, include all data attributes. Match the existing format.
- Books are sorted by `data-year` within each section.
- `&` must be escaped as `&amp;` in HTML.
- Sections: Picture Books, Chapter Books, Poetry Books.
- Meditations is in Chapter Books, not Poetry.
- Use first publication date. For translations: `(YEAR, English translation YEAR)`.
- **Credits:** Solo author-illustrators get plain `by Name`. Collaborations get explicit role labels: `by Name (Author), Name (Illustrator)`.

## When adding a book

1. Add the `<li>` in the correct year-sorted position within its section.
2. Include all data attributes (`data-year`, `data-status`, `data-added` with today's date, `data-starred` if applicable).
3. If the book has awards, add `data-caldecott-medal`, `data-caldecott-honor`, and/or `data-nyt-illustrated` attributes, AND add a `title` attribute on the `<cite>` element (e.g. `<cite title="Caldecott Medal 2019">`).
4. Add an `<item>` to the top of `feed.xml` with the book title, author, a `<guid>` (slug-year), and `<pubDate>` (date you're adding it, RFC 822 format, e.g. `Fri, 28 Feb 2026 00:00:00 +0000`). If the book is starred, also add it to `starred.xml`.
5. Check if the book was recommended via a GitHub issue (`gh search issues` in the repo). If it was:
   - Add an inline thank-you in the `<li>`, e.g. `Thanks to <a href="https://github.com/callicles">@callicles</a> for the recommendation!`
   - After committing, close the issue with a comment referencing the commit (e.g. `gh issue close N --comment "Added in <commit-sha>. Thanks for the recommendation!"`)

## When adding or removing a page

- Add/remove a `<url>` entry in `sitemap.xml` with the page URL and today's date as `<lastmod>`.
- Do not include non-public pages (e.g. `webring-mock.html`) in the sitemap.

## TODOs

- ~~Add `<details>` collapsible sections~~ (done: easter egg in footer)

## Future ideas

- ~~"Starred" page with a line or two about each starred book~~ (done: starred.html)
- Book / star count on the correlations (stats) page
- Standardize page footers across all pages
- Better navigation between pages
- ~~Auto-discover pages for sitemap.xml~~ (done: manual, instructions in "When adding or removing a page")
- SEO best practices audit
- ~~Index page: sort and filter controls~~ (done: pill buttons for starred/awarded/sort)
- Index page typography audit: line spacing, indentation, rich data layout, mobile readability
- Favorite libraries section
- More awards (Newbery, etc.) — Greenaway and CBCA checklists already added
