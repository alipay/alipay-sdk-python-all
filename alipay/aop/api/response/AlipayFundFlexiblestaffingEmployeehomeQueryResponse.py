#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EmployeeCardInfoResDTO import EmployeeCardInfoResDTO
from alipay.aop.api.domain.RentAgreementInfoDTO import RentAgreementInfoDTO
from alipay.aop.api.domain.RentServiceInfoDTO import RentServiceInfoDTO


class AlipayFundFlexiblestaffingEmployeehomeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundFlexiblestaffingEmployeehomeQueryResponse, self).__init__()
        self._apply_status = None
        self._biz_scene = None
        self._employee_card_info = None
        self._out_biz_no = None
        self._product_code = None
        self._rent_agreement_info = None
        self._rent_service_info = None

    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def employee_card_info(self):
        return self._employee_card_info

    @employee_card_info.setter
    def employee_card_info(self, value):
        if isinstance(value, EmployeeCardInfoResDTO):
            self._employee_card_info = value
        else:
            self._employee_card_info = EmployeeCardInfoResDTO.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def rent_agreement_info(self):
        return self._rent_agreement_info

    @rent_agreement_info.setter
    def rent_agreement_info(self, value):
        if isinstance(value, RentAgreementInfoDTO):
            self._rent_agreement_info = value
        else:
            self._rent_agreement_info = RentAgreementInfoDTO.from_alipay_dict(value)
    @property
    def rent_service_info(self):
        return self._rent_service_info

    @rent_service_info.setter
    def rent_service_info(self, value):
        if isinstance(value, RentServiceInfoDTO):
            self._rent_service_info = value
        else:
            self._rent_service_info = RentServiceInfoDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayFundFlexiblestaffingEmployeehomeQueryResponse, self).parse_response_content(response_content)
        if 'apply_status' in response:
            self.apply_status = response['apply_status']
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'employee_card_info' in response:
            self.employee_card_info = response['employee_card_info']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'product_code' in response:
            self.product_code = response['product_code']
        if 'rent_agreement_info' in response:
            self.rent_agreement_info = response['rent_agreement_info']
        if 'rent_service_info' in response:
            self.rent_service_info = response['rent_service_info']
