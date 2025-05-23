#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ConvertedDetail import ConvertedDetail


class AlipayDataDataserviceAdconversionConversionidQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdconversionConversionidQueryResponse, self).__init__()
        self._converted_detail_list = None

    @property
    def converted_detail_list(self):
        return self._converted_detail_list

    @converted_detail_list.setter
    def converted_detail_list(self, value):
        if isinstance(value, list):
            self._converted_detail_list = list()
            for i in value:
                if isinstance(i, ConvertedDetail):
                    self._converted_detail_list.append(i)
                else:
                    self._converted_detail_list.append(ConvertedDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdconversionConversionidQueryResponse, self).parse_response_content(response_content)
        if 'converted_detail_list' in response:
            self.converted_detail_list = response['converted_detail_list']
