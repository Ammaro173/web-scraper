from web_scraper.web_scraper import (
    get_citations_needed_report,
    get_citations_needed_count,
)


# test for count of citations
def test_get_citations_needed_count():
    url = "https://en.wikipedia.org/wiki/History_of_Mexico"
    actual = get_citations_needed_count(url)
    expected = 5
    assert actual == expected


# test for ciations needed report , Remeber the \n !! in the stored varaible its being checked !!
def test_get_citations_needed_report():
    url = "https://en.wikipedia.org/wiki/History_of_Mexico"
    actual = get_citations_needed_report(url)
    expected = """\n ==> ) surrounded by dense forest. Deer were found in this area, but most fauna were small land animals and fish and other lacustrine animals were found in the lake region.[citation needed] .\n ==> The Mexica people arrived in the Valley of Mexico in 1248 AD. They had migrated from the deserts north of the Rio Grande[citation needed] .\n ==>  over a period traditionally said to have been 100 years. They may have thought of themselves as the heirs to the prestigious civilizations that had preceded them.[citation needed] .\n ==> The Spanish had no intention to turn over Tenochtitlan to the Tlaxcalteca. While Tlaxcalteca troops continued to help the Spaniards, and Tlaxcala received better treatment than other indigenous nations, the Spanish eventually disowned the treaty. Forty years after the conquest, the Tlaxcalteca had to pay the same tax as any other indigenous community.[citation needed] .\n ==> During the three centuries of colonial rule, fewer than 700,000 Spaniards, most of them men, settled in Mexico.[citation needed] ."""
    assert actual == expected
