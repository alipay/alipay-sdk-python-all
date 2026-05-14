#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsuranceMedicineInfo import InsuranceMedicineInfo
from alipay.aop.api.domain.OutletInfo import OutletInfo


class AlipayCommerceMedicalInsuranceTpadirectpaystatusSyncModel(object):

    def __init__(self):
        self._claim_application = None
        self._code_data = None
        self._event_type = None
        self._ext_data = None
        self._individual_policy_no = None
        self._medicine_list = None
        self._need_self_pay = None
        self._open_id = None
        self._order_amount = None
        self._order_no = None
        self._order_time = None
        self._order_type = None
        self._outlet_info = None
        self._policy_no = None
        self._recipe_image = None
        self._refund_amount = None
        self._tpa_id = None
        self._user_id = None

    @property
    def claim_application(self):
        return self._claim_application

    @claim_application.setter
    def claim_application(self, value):
        self._claim_application = value
    @property
    def code_data(self):
        return self._code_data

    @code_data.setter
    def code_data(self, value):
        self._code_data = value
    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def ext_data(self):
        return self._ext_data

    @ext_data.setter
    def ext_data(self, value):
        self._ext_data = value
    @property
    def individual_policy_no(self):
        return self._individual_policy_no

    @individual_policy_no.setter
    def individual_policy_no(self, value):
        self._individual_policy_no = value
    @property
    def medicine_list(self):
        return self._medicine_list

    @medicine_list.setter
    def medicine_list(self, value):
        if isinstance(value, list):
            self._medicine_list = list()
            for i in value:
                if isinstance(i, InsuranceMedicineInfo):
                    self._medicine_list.append(i)
                else:
                    self._medicine_list.append(InsuranceMedicineInfo.from_alipay_dict(i))
    @property
    def need_self_pay(self):
        return self._need_self_pay

    @need_self_pay.setter
    def need_self_pay(self, value):
        self._need_self_pay = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def outlet_info(self):
        return self._outlet_info

    @outlet_info.setter
    def outlet_info(self, value):
        if isinstance(value, OutletInfo):
            self._outlet_info = value
        else:
            self._outlet_info = OutletInfo.from_alipay_dict(value)
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def recipe_image(self):
        return self._recipe_image

    @recipe_image.setter
    def recipe_image(self, value):
        self._recipe_image = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def tpa_id(self):
        return self._tpa_id

    @tpa_id.setter
    def tpa_id(self, value):
        self._tpa_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.claim_application:
            if hasattr(self.claim_application, 'to_alipay_dict'):
                params['claim_application'] = self.claim_application.to_alipay_dict()
            else:
                params['claim_application'] = self.claim_application
        if self.code_data:
            if hasattr(self.code_data, 'to_alipay_dict'):
                params['code_data'] = self.code_data.to_alipay_dict()
            else:
                params['code_data'] = self.code_data
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        if self.ext_data:
            if hasattr(self.ext_data, 'to_alipay_dict'):
                params['ext_data'] = self.ext_data.to_alipay_dict()
            else:
                params['ext_data'] = self.ext_data
        if self.individual_policy_no:
            if hasattr(self.individual_policy_no, 'to_alipay_dict'):
                params['individual_policy_no'] = self.individual_policy_no.to_alipay_dict()
            else:
                params['individual_policy_no'] = self.individual_policy_no
        if self.medicine_list:
            if isinstance(self.medicine_list, list):
                for i in range(0, len(self.medicine_list)):
                    element = self.medicine_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.medicine_list[i] = element.to_alipay_dict()
            if hasattr(self.medicine_list, 'to_alipay_dict'):
                params['medicine_list'] = self.medicine_list.to_alipay_dict()
            else:
                params['medicine_list'] = self.medicine_list
        if self.need_self_pay:
            if hasattr(self.need_self_pay, 'to_alipay_dict'):
                params['need_self_pay'] = self.need_self_pay.to_alipay_dict()
            else:
                params['need_self_pay'] = self.need_self_pay
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.order_time:
            if hasattr(self.order_time, 'to_alipay_dict'):
                params['order_time'] = self.order_time.to_alipay_dict()
            else:
                params['order_time'] = self.order_time
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.outlet_info:
            if hasattr(self.outlet_info, 'to_alipay_dict'):
                params['outlet_info'] = self.outlet_info.to_alipay_dict()
            else:
                params['outlet_info'] = self.outlet_info
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        if self.recipe_image:
            if hasattr(self.recipe_image, 'to_alipay_dict'):
                params['recipe_image'] = self.recipe_image.to_alipay_dict()
            else:
                params['recipe_image'] = self.recipe_image
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.tpa_id:
            if hasattr(self.tpa_id, 'to_alipay_dict'):
                params['tpa_id'] = self.tpa_id.to_alipay_dict()
            else:
                params['tpa_id'] = self.tpa_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInsuranceTpadirectpaystatusSyncModel()
        if 'claim_application' in d:
            o.claim_application = d['claim_application']
        if 'code_data' in d:
            o.code_data = d['code_data']
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'ext_data' in d:
            o.ext_data = d['ext_data']
        if 'individual_policy_no' in d:
            o.individual_policy_no = d['individual_policy_no']
        if 'medicine_list' in d:
            o.medicine_list = d['medicine_list']
        if 'need_self_pay' in d:
            o.need_self_pay = d['need_self_pay']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'order_time' in d:
            o.order_time = d['order_time']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'outlet_info' in d:
            o.outlet_info = d['outlet_info']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'recipe_image' in d:
            o.recipe_image = d['recipe_image']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'tpa_id' in d:
            o.tpa_id = d['tpa_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


