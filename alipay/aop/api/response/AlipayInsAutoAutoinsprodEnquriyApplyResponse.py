#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CarModel import CarModel


class AlipayInsAutoAutoinsprodEnquriyApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsAutoAutoinsprodEnquriyApplyResponse, self).__init__()
        self._car_model = None
        self._enquiry_biz_id = None
        self._out_biz_no = None

    @property
    def car_model(self):
        return self._car_model

    @car_model.setter
    def car_model(self, value):
        if isinstance(value, list):
            self._car_model = list()
            for i in value:
                if isinstance(i, CarModel):
                    self._car_model.append(i)
                else:
                    self._car_model.append(CarModel.from_alipay_dict(i))
    @property
    def enquiry_biz_id(self):
        return self._enquiry_biz_id

    @enquiry_biz_id.setter
    def enquiry_biz_id(self, value):
        self._enquiry_biz_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsAutoAutoinsprodEnquriyApplyResponse, self).parse_response_content(response_content)
        if 'car_model' in response:
            self.car_model = response['car_model']
        if 'enquiry_biz_id' in response:
            self.enquiry_biz_id = response['enquiry_biz_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
