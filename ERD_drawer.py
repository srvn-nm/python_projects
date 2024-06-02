from graphviz import Digraph

# Create a new directed graph
dot = Digraph()

# Define nodes
dot.node('Customer', 'Customer\nCustomerID (PK)\nFirstName\nLastName\nPhoneNumber')
dot.node('Request', 'Request\nRequestID (PK)\nCustomerID (FK)\nURLID (FK)\nStatusID (FK)')
dot.node('Invoice', 'Invoice\nInvoiceID (PK)\nRequestID (FK)\nAmount\nCustomerID (FK)')
dot.node('URL', 'URL\nURLID (PK)\nOriginalURL\nCreatedAt')
dot.node('ShortenedURL', 'Shortened URL\nShortenedURLID (PK)\nShortenedURL\nCreatedAt')
dot.node('DeletedURLs', 'Deleted URLs\nDeletedURLID (PK)\nShortenedURLID (FK)\nDeletedAt')
dot.node('RequestStatus', 'Request Status\nStatusID (PK)\nStatusName')
dot.node('FAQ', 'FAQ\nFAQID (PK)\nTitle')
dot.node('FAQEntry', 'FAQ Entry\nFAQEntryID (PK)\nFAQID (FK)\nAuthorName\nQuestion\nAnswer')

# Define edges (relationships)
dot.edge('Customer', 'Request', label='1 to N')
dot.edge('Request', 'Invoice', label='1 to 1')
dot.edge('Request', 'URL', label='1 to 1')
dot.edge('URL', 'ShortenedURL', label='1 to 1')
dot.edge('ShortenedURL', 'DeletedURLs', label='1 to 1')
dot.edge('Request', 'RequestStatus', label='1 to 1')
dot.edge('Customer', 'Invoice', label='1 to N')
dot.edge('Customer', 'FAQEntry', label='1 to N')
dot.edge('FAQ', 'FAQEntry', label='1 to N')

# Render the graph to a file
dot.render('tinyURL_ERD', format='png', cleanup=False)

# Display the graph in Jupyter Notebook (if using Jupyter)
dot.view()
