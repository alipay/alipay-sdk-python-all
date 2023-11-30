#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EmployeeCardInfoDTO import EmployeeCardInfoDTO
from alipay.aop.api.domain.InsureAttendDTO import InsureAttendDTO
from alipay.aop.api.domain.InsureInfoDTO import InsureInfoDTO
from alipay.aop.api.domain.InsurePartnerOrganization import InsurePartnerOrganization


class AlipayFundFlexiblestaffingAttendanceApplyModel(object):

    def __init__(self):
        self._apply_link_type = None
        self._biz_scene = None
        self._channel = None
        self._employee_card_info = None
        self._expire_time = None
        self._insure_attend = None
        self._insure_info = None
        self._insure_type = None
        self._job_list = None
        self._out_biz_no = None
        self._partner_organization = None
        self._product_code = None

    @property
    def apply_link_type(self):
        return self._apply_link_type

    @apply_link_type.setter
    def apply_link_type(self, value):
        self._apply_link_type = value
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
        if isinstance(value, EmployeeCardInfoDTO):
            self._employee_card_info = value
        else:
            self._employee_card_info = EmployeeCardInfoDTO.from_alipay_dict(value)
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def insure_attend(self):
        return self._insure_attend

    @insure_attend.setter
    def insure_attend(self, value):
        if isinstance(value, InsureAttendDTO):
            self._insure_attend = value
        else:
            self._insure_attend = InsureAttendDTO.from_alipay_dict(value)
    @property
    def insure_info(self):
        return self._insure_info

    @insure_info.setter
    def insure_info(self, value):
        if isinstance(value, InsureInfoDTO):
            self._insure_info = value
        else:
            self._insure_info = InsureInfoDTO.from_alipay_dict(value)
    @property
    def insure_type(self):
        return self._insure_type

    @insure_type.setter
    def insure_type(self, value):
        self._insure_type = value
    @property
    def job_list(self):
        return self._job_list

    @job_list.setter
    def job_list(self, value):
        if isinstance(value, list):
            self._job_list = list()
            for i in value:
                self._job_list.append(i)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_organization(self):
        return self._partner_organization

    @partner_organization.setter
    def partner_organization(self, value):
        if isinstance(value, InsurePartnerOrganization):
            self._partner_organization = value
        else:
            self._partner_organization = InsurePartnerOrganization.from_alipay_dict(value)
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_link_type:
            if hasattr(self.apply_link_type, 'to_alipay_dict'):
                params['apply_link_type'] = self.apply_link_type.to_alipay_dict()
            else:
                params['apply_link_type'] = self.apply_link_type
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
        if self.insure_attend:
            if hasattr(self.insure_attend, 'to_alipay_dict'):
                params['insure_attend'] = self.insure_attend.to_alipay_dict()
            else:
                params['insure_attend'] = self.insure_attend
        if self.insure_info:
            if hasattr(self.insure_info, 'to_alipay_dict'):
                params['insure_info'] = self.insure_info.to_alipay_dict()
            else:
                params['insure_info'] = self.insure_info
        if self.insure_type:
            if hasattr(self.insure_type, 'to_alipay_dict'):
                params['insure_type'] = self.insure_type.to_alipay_dict()
            else:
                params['insure_type'] = self.insure_type
        if self.job_list:
            if isinstance(self.job_list, list):
                for i in range(0, len(self.job_list)):
                    element = self.job_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.job_list[i] = element.to_alipay_dict()
            if hasattr(self.job_list, 'to_alipay_dict'):
                params['job_list'] = self.job_list.to_alipay_dict()
            else:
                params['job_list'] = self.job_list
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.partner_organization:
            if hasattr(self.partner_organization, 'to_alipay_dict'):
                params['partner_organization'] = self.partner_organization.to_alipay_dict()
            else:
                params['partner_organization'] = self.partner_organization
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundFlexiblestaffingAttendanceApplyModel()
        if 'apply_link_type' in d:
            o.apply_link_type = d['apply_link_type']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'channel' in d:
            o.channel = d['channel']
        if 'employee_card_info' in d:
            o.employee_card_info = d['employee_card_info']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'insure_attend' in d:
            o.insure_attend = d['insure_attend']
        if 'insure_info' in d:
            o.insure_info = d['insure_info']
        if 'insure_type' in d:
            o.insure_type = d['insure_type']
        if 'job_list' in d:
            o.job_list = d['job_list']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_organization' in d:
            o.partner_organization = d['partner_organization']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


