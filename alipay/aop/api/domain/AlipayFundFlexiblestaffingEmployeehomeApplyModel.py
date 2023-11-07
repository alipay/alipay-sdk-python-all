#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EmployeeCardInfo import EmployeeCardInfo
from alipay.aop.api.domain.ParticipantInfoDTO import ParticipantInfoDTO
from alipay.aop.api.domain.RentServiceInfo import RentServiceInfo


class AlipayFundFlexiblestaffingEmployeehomeApplyModel(object):

    def __init__(self):
        self._apply_link_type = None
        self._back_url = None
        self._biz_scene = None
        self._channel = None
        self._employee_card_info = None
        self._expire_time = None
        self._out_biz_no = None
        self._principal_info = None
        self._product_code = None
        self._rent_agreement_info = None

    @property
    def apply_link_type(self):
        return self._apply_link_type

    @apply_link_type.setter
    def apply_link_type(self, value):
        self._apply_link_type = value
    @property
    def back_url(self):
        return self._back_url

    @back_url.setter
    def back_url(self, value):
        self._back_url = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def employee_card_info(self):
        return self._employee_card_info

    @employee_card_info.setter
    def employee_card_info(self, value):
        if isinstance(value, EmployeeCardInfo):
            self._employee_card_info = value
        else:
            self._employee_card_info = EmployeeCardInfo.from_alipay_dict(value)
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def principal_info(self):
        return self._principal_info

    @principal_info.setter
    def principal_info(self, value):
        if isinstance(value, ParticipantInfoDTO):
            self._principal_info = value
        else:
            self._principal_info = ParticipantInfoDTO.from_alipay_dict(value)
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
        if isinstance(value, RentServiceInfo):
            self._rent_agreement_info = value
        else:
            self._rent_agreement_info = RentServiceInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.apply_link_type:
            if hasattr(self.apply_link_type, 'to_alipay_dict'):
                params['apply_link_type'] = self.apply_link_type.to_alipay_dict()
            else:
                params['apply_link_type'] = self.apply_link_type
        if self.back_url:
            if hasattr(self.back_url, 'to_alipay_dict'):
                params['back_url'] = self.back_url.to_alipay_dict()
            else:
                params['back_url'] = self.back_url
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.employee_card_info:
            if hasattr(self.employee_card_info, 'to_alipay_dict'):
                params['employee_card_info'] = self.employee_card_info.to_alipay_dict()
            else:
                params['employee_card_info'] = self.employee_card_info
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.principal_info:
            if hasattr(self.principal_info, 'to_alipay_dict'):
                params['principal_info'] = self.principal_info.to_alipay_dict()
            else:
                params['principal_info'] = self.principal_info
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.rent_agreement_info:
            if hasattr(self.rent_agreement_info, 'to_alipay_dict'):
                params['rent_agreement_info'] = self.rent_agreement_info.to_alipay_dict()
            else:
                params['rent_agreement_info'] = self.rent_agreement_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundFlexiblestaffingEmployeehomeApplyModel()
        if 'apply_link_type' in d:
            o.apply_link_type = d['apply_link_type']
        if 'back_url' in d:
            o.back_url = d['back_url']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'channel' in d:
            o.channel = d['channel']
        if 'employee_card_info' in d:
            o.employee_card_info = d['employee_card_info']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'principal_info' in d:
            o.principal_info = d['principal_info']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'rent_agreement_info' in d:
            o.rent_agreement_info = d['rent_agreement_info']
        return o


