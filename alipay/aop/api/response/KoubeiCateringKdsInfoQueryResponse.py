#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KdsInfoModel import KdsInfoModel


class KoubeiCateringKdsInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringKdsInfoQueryResponse, self).__init__()
        self._kds_info_model_list = None

    @property
    def kds_info_model_list(self):
        return self._kds_info_model_list

    @kds_info_model_list.setter
    def kds_info_model_list(self, value):
        if isinstance(value, list):
            self._kds_info_model_list = list()
            for i in value:
                if isinstance(i, KdsInfoModel):
                    self._kds_info_model_list.append(i)
                else:
                    self._kds_info_model_list.append(KdsInfoModel.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringKdsInfoQueryResponse, self).parse_response_content(response_content)
        if 'kds_info_model_list' in response:
            self.kds_info_model_list = response['kds_info_model_list']
