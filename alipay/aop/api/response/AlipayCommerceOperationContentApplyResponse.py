#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OperationExtDataModel import OperationExtDataModel


class AlipayCommerceOperationContentApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationContentApplyResponse, self).__init__()
        self._ext_data = None
        self._out_biz_no = None
        self._record_id = None
        self._target_id = None

    @property
    def ext_data(self):
        return self._ext_data

    @ext_data.setter
    def ext_data(self, value):
        if isinstance(value, OperationExtDataModel):
            self._ext_data = value
        else:
            self._ext_data = OperationExtDataModel.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def target_id(self):
        return self._target_id

    @target_id.setter
    def target_id(self, value):
        self._target_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationContentApplyResponse, self).parse_response_content(response_content)
        if 'ext_data' in response:
            self.ext_data = response['ext_data']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'record_id' in response:
            self.record_id = response['record_id']
        if 'target_id' in response:
            self.target_id = response['target_id']
