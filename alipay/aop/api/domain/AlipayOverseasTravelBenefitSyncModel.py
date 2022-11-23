#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BenefitCodeInfoDTO import BenefitCodeInfoDTO
from alipay.aop.api.domain.BenefitDeliveryInfoDTO import BenefitDeliveryInfoDTO
from alipay.aop.api.domain.BenefitDisplayInfoDTO import BenefitDisplayInfoDTO
from alipay.aop.api.domain.BenefitSendRuleDTO import BenefitSendRuleDTO
from alipay.aop.api.domain.BenefitUseRuleDTO import BenefitUseRuleDTO
from alipay.aop.api.domain.MerchantInfoDTO import MerchantInfoDTO


class AlipayOverseasTravelBenefitSyncModel(object):

    def __init__(self):
        self._benefit_code_info = None
        self._benefit_delivery_info = None
        self._benefit_display_info = None
        self._benefit_id = None
        self._benefit_send_rule = None
        self._benefit_type = None
        self._benefit_use_rule = None
        self._description = None
        self._end_time = None
        self._ext_info = None
        self._merchant_info = None
        self._name = None
        self._out_biz_no = None
        self._source = None
        self._start_time = None
        self._status = None

    @property
    def benefit_code_info(self):
        return self._benefit_code_info

    @benefit_code_info.setter
    def benefit_code_info(self, value):
        if isinstance(value, BenefitCodeInfoDTO):
            self._benefit_code_info = value
        else:
            self._benefit_code_info = BenefitCodeInfoDTO.from_alipay_dict(value)
    @property
    def benefit_delivery_info(self):
        return self._benefit_delivery_info

    @benefit_delivery_info.setter
    def benefit_delivery_info(self, value):
        if isinstance(value, BenefitDeliveryInfoDTO):
            self._benefit_delivery_info = value
        else:
            self._benefit_delivery_info = BenefitDeliveryInfoDTO.from_alipay_dict(value)
    @property
    def benefit_display_info(self):
        return self._benefit_display_info

    @benefit_display_info.setter
    def benefit_display_info(self, value):
        if isinstance(value, BenefitDisplayInfoDTO):
            self._benefit_display_info = value
        else:
            self._benefit_display_info = BenefitDisplayInfoDTO.from_alipay_dict(value)
    @property
    def benefit_id(self):
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, value):
        self._benefit_id = value
    @property
    def benefit_send_rule(self):
        return self._benefit_send_rule

    @benefit_send_rule.setter
    def benefit_send_rule(self, value):
        if isinstance(value, BenefitSendRuleDTO):
            self._benefit_send_rule = value
        else:
            self._benefit_send_rule = BenefitSendRuleDTO.from_alipay_dict(value)
    @property
    def benefit_type(self):
        return self._benefit_type

    @benefit_type.setter
    def benefit_type(self, value):
        self._benefit_type = value
    @property
    def benefit_use_rule(self):
        return self._benefit_use_rule

    @benefit_use_rule.setter
    def benefit_use_rule(self, value):
        if isinstance(value, BenefitUseRuleDTO):
            self._benefit_use_rule = value
        else:
            self._benefit_use_rule = BenefitUseRuleDTO.from_alipay_dict(value)
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def merchant_info(self):
        return self._merchant_info

    @merchant_info.setter
    def merchant_info(self, value):
        if isinstance(value, MerchantInfoDTO):
            self._merchant_info = value
        else:
            self._merchant_info = MerchantInfoDTO.from_alipay_dict(value)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_code_info:
            if hasattr(self.benefit_code_info, 'to_alipay_dict'):
                params['benefit_code_info'] = self.benefit_code_info.to_alipay_dict()
            else:
                params['benefit_code_info'] = self.benefit_code_info
        if self.benefit_delivery_info:
            if hasattr(self.benefit_delivery_info, 'to_alipay_dict'):
                params['benefit_delivery_info'] = self.benefit_delivery_info.to_alipay_dict()
            else:
                params['benefit_delivery_info'] = self.benefit_delivery_info
        if self.benefit_display_info:
            if hasattr(self.benefit_display_info, 'to_alipay_dict'):
                params['benefit_display_info'] = self.benefit_display_info.to_alipay_dict()
            else:
                params['benefit_display_info'] = self.benefit_display_info
        if self.benefit_id:
            if hasattr(self.benefit_id, 'to_alipay_dict'):
                params['benefit_id'] = self.benefit_id.to_alipay_dict()
            else:
                params['benefit_id'] = self.benefit_id
        if self.benefit_send_rule:
            if hasattr(self.benefit_send_rule, 'to_alipay_dict'):
                params['benefit_send_rule'] = self.benefit_send_rule.to_alipay_dict()
            else:
                params['benefit_send_rule'] = self.benefit_send_rule
        if self.benefit_type:
            if hasattr(self.benefit_type, 'to_alipay_dict'):
                params['benefit_type'] = self.benefit_type.to_alipay_dict()
            else:
                params['benefit_type'] = self.benefit_type
        if self.benefit_use_rule:
            if hasattr(self.benefit_use_rule, 'to_alipay_dict'):
                params['benefit_use_rule'] = self.benefit_use_rule.to_alipay_dict()
            else:
                params['benefit_use_rule'] = self.benefit_use_rule
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.merchant_info:
            if hasattr(self.merchant_info, 'to_alipay_dict'):
                params['merchant_info'] = self.merchant_info.to_alipay_dict()
            else:
                params['merchant_info'] = self.merchant_info
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTravelBenefitSyncModel()
        if 'benefit_code_info' in d:
            o.benefit_code_info = d['benefit_code_info']
        if 'benefit_delivery_info' in d:
            o.benefit_delivery_info = d['benefit_delivery_info']
        if 'benefit_display_info' in d:
            o.benefit_display_info = d['benefit_display_info']
        if 'benefit_id' in d:
            o.benefit_id = d['benefit_id']
        if 'benefit_send_rule' in d:
            o.benefit_send_rule = d['benefit_send_rule']
        if 'benefit_type' in d:
            o.benefit_type = d['benefit_type']
        if 'benefit_use_rule' in d:
            o.benefit_use_rule = d['benefit_use_rule']
        if 'description' in d:
            o.description = d['description']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'merchant_info' in d:
            o.merchant_info = d['merchant_info']
        if 'name' in d:
            o.name = d['name']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'source' in d:
            o.source = d['source']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        return o


