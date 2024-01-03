#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AiPicture import AiPicture


class AlipayUserAigcAipictureBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAigcAipictureBatchqueryResponse, self).__init__()
        self._pic_list = None

    @property
    def pic_list(self):
        return self._pic_list

    @pic_list.setter
    def pic_list(self, value):
        if isinstance(value, list):
            self._pic_list = list()
            for i in value:
                if isinstance(i, AiPicture):
                    self._pic_list.append(i)
                else:
                    self._pic_list.append(AiPicture.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayUserAigcAipictureBatchqueryResponse, self).parse_response_content(response_content)
        if 'pic_list' in response:
            self.pic_list = response['pic_list']
