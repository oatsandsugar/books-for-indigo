<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:s="http://www.sitemaps.org/schemas/sitemap/0.9">
<xsl:output method="html" encoding="UTF-8" indent="yes"/>
<xsl:template match="/">
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="color-scheme" content="dark light"/>
  <title>Sitemap — Books for Indigo</title>
  <style>body { font-family: monospace; }</style>
</head>
<body>
  <h1>Sitemap</h1>
  <p><a href="/">← Books for Indigo</a></p>
  <ul>
    <xsl:for-each select="s:urlset/s:url">
      <li><a href="{s:loc}"><xsl:value-of select="s:loc"/></a></li>
    </xsl:for-each>
  </ul>
</body>
</html>
</xsl:template>
</xsl:stylesheet>
