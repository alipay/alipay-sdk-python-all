#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BoothContentInfoModel import BoothContentInfoModel
from alipay.aop.api.domain.OperationExtDataModel import OperationExtDataModel


class AlipayCommerceOperationContentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationContentQueryResponse, self).__init__()
        self._content_infos = None
        self._ext_data = None

    @property
    def content_infos(self):
        return self._content_infos

    @content_infos.setter
    def content_infos(self, value):
        if isinstance(value, list):
            self._content_infos = list()
            for i in value:
                if isinstance(i, BoothContentInfoModel):
                    self._content_infos.append(i)
                else:
                    self._content_infos.append(BoothContentInfoModel.from_alipay_dict(i))
    @property
    def ext_data(self):
        return self._ext_data

    @ext_data.setter
    def ext_data(self, value):
        if isinstance(value, OperationExtDataModel):
            self._ext_data = value
        else:
            self._ext_data = OperationExtDataModel.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationContentQueryResponse, self).parse_response_content(response_content)
        if 'content_infos' in response:
            self.content_infos = response['content_infos']
        if 'ext_data' in response:
            self.ext_data = response['ext_data']
