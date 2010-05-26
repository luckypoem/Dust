from util.jsonrpc.proxy import ServiceProxy

class DustmailClient(ServiceProxy):
  def __init__(self, router, addr):
    ServiceProxy.__init__(self, router, addr=addr, serviceName="dustmail")
