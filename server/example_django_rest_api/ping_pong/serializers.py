from rest_framework import serializers


class PingPongSerializer(serializers.Serializer):
    ping = serializers.CharField(allow_blank=True,
                                 default="ping",
                                 max_length=10,
                                 help_text="please input 'ping'")

# example_ping = PingPongSerializer({"ping": "hoge"})
# => {'ping' : 'hoge'}
# example_ping = PingPongSerializer({})
# print(example_ping.data)
# => {'ping' : 'hoge'}
