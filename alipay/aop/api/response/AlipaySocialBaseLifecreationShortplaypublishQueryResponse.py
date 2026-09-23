#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ShortPlayChannelInfo import ShortPlayChannelInfo


class AlipaySocialBaseLifecreationShortplaypublishQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseLifecreationShortplaypublishQueryResponse, self).__init__()
        self._album_id = None
        self._publish_info_list = None

    @property
    def album_id(self):
        return self._album_id

    @album_id.setter
    def album_id(self, value):
        self._album_id = value
    @property
    def publish_info_list(self):
        return self._publish_info_list

    @publish_info_list.setter
    def publish_info_list(self, value):
        if isinstance(value, list):
            self._publish_info_list = list()
            for i in value:
                if isinstance(i, ShortPlayChannelInfo):
                    self._publish_info_list.append(i)
                else:
                    self._publish_info_list.append(ShortPlayChannelInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseLifecreationShortplaypublishQueryResponse, self).parse_response_content(response_content)
        if 'album_id' in response:
            self.album_id = response['album_id']
        if 'publish_info_list' in response:
            self.publish_info_list = response['publish_info_list']
