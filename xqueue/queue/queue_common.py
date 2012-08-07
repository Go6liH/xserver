#
# Xqueue header/body/footer convention is as follows:
#
#   Header: Routing information (callback id and secret key) between 
#               LMS <--> Xqueue, and Xqueue <--> External grader
#   Body:   Serialized message between LMS <--> External grader
#               (Contents will NOT be modified by Xqueue)
#   Footer: Metadata used only WITHIN Xqueue 
#
HEADER_TAG = 'xqueue_header'
BODY_TAG   = 'xqueue_body'
FOOTER_TAG = 'xqueue_footer'

RABBIT_HOST = 'localhost'
QUEUES = ['MITx-6.00x', 'python', 'null']
