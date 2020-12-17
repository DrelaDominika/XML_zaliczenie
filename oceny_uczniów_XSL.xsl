<?xml version="1.0" encoding="ISO-8859-1"?>               
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="Klasy">
    <html> 
      <head> 
        <title>Oceny uczniow </title>
     </head>
     <body text="black">
		<img src="mojdziennik.png"/>
		<xsl:for-each select="uczniowie">
			<h1>Oceny uczniow klasy <xsl:value-of select="@klasa"/></h1>
			<table border="1">
				<tr bgcolor="#CC99CC">
					<th>Uczen</th>
					<th>Polski</th>
					<th>Angielski</th>
					<th>Matematyka</th>
					<th>Fizyka</th>
					<th>Geografia</th>
				</tr>
				<xsl:for-each select="uczen">
				<xsl:sort select="nazwisko"/>
				<tr>
					<td bgcolor="#EEEEEE"><xsl:value-of select="imie"/> <xsl:text> </xsl:text> <xsl:value-of select="nazwisko"/></td>
					<xsl:for-each select="przedmioty">
					<td><xsl:value-of select="polski"/></td>
					<td><xsl:value-of select="angielski"/></td>
					<td><xsl:value-of select="matematyka"/></td>
					<td><xsl:value-of select="fizyka"/></td>
					<td><xsl:value-of select="geografia"/></td>
					</xsl:for-each>
				</tr>
				</xsl:for-each>
				</table>
				</xsl:for-each>
			 </body>
			</html> 
		   </xsl:template>
		</xsl:stylesheet> 