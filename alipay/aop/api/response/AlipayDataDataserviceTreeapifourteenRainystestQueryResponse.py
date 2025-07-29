#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RainyComplexTypesTheFourteen import RainyComplexTypesTheFourteen
from alipay.aop.api.domain.RainyComplexTypesTheFourteen import RainyComplexTypesTheFourteen


class AlipayDataDataserviceTreeapifourteenRainystestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceTreeapifourteenRainystestQueryResponse, self).__init__()
        self._demo_case = None
        self._res_copy_weak_ref = None
        self._res_field_weak_ref = None
        self._user_id = None

    @property
    def demo_case(self):
        return self._demo_case

    @demo_case.setter
    def demo_case(self, value):
        self._demo_case = value
    @property
    def res_copy_weak_ref(self):
        return self._res_copy_weak_ref

    @res_copy_weak_ref.setter
    def res_copy_weak_ref(self, value):
        if isinstance(value, RainyComplexTypesTheFourteen):
            self._res_copy_weak_ref = value
        else:
            self._res_copy_weak_ref = RainyComplexTypesTheFourteen.from_alipay_dict(value)
    @property
    def res_field_weak_ref(self):
        return self._res_field_weak_ref

    @res_field_weak_ref.setter
    def res_field_weak_ref(self, value):
        if isinstance(value, RainyComplexTypesTheFourteen):
            self._res_field_weak_ref = value
        else:
            self._res_field_weak_ref = RainyComplexTypesTheFourteen.from_alipay_dict(value)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceTreeapifourteenRainystestQueryResponse, self).parse_response_content(response_content)
        if 'demo_case' in response:
            self.demo_case = response['demo_case']
        if 'res_copy_weak_ref' in response:
            self.res_copy_weak_ref = response['res_copy_weak_ref']
        if 'res_field_weak_ref' in response:
            self.res_field_weak_ref = response['res_field_weak_ref']
        if 'user_id' in response:
            self.user_id = response['user_id']
