#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MExtInfo import MExtInfo
from alipay.aop.api.domain.MPromoInfo import MPromoInfo


class KoubeiMarketingCampaignMerchantActivityCreateModel(object):

    def __init__(self):
        self._auto_delay_flag = None
        self._biz_scene = None
        self._desc = None
        self._end_time = None
        self._ext_info = None
        self._name = None
        self._operator = None
        self._operator_type = None
        self._out_biz_type = None
        self._out_request_no = None
        self._promo_info_list = None
        self._start_time = None

    @property
    def auto_delay_flag(self):
        return self._auto_delay_flag

    @auto_delay_flag.setter
    def auto_delay_flag(self, value):
        self._auto_delay_flag = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
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
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, MExtInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(MExtInfo.from_alipay_dict(i))
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def operator_type(self):
        return self._operator_type

    @operator_type.setter
    def operator_type(self, value):
        self._operator_type = value
    @property
    def out_biz_type(self):
        return self._out_biz_type

    @out_biz_type.setter
    def out_biz_type(self, value):
        self._out_biz_type = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def promo_info_list(self):
        return self._promo_info_list

    @promo_info_list.setter
    def promo_info_list(self, value):
        if isinstance(value, list):
            self._promo_info_list = list()
            for i in value:
                if isinstance(i, MPromoInfo):
                    self._promo_info_list.append(i)
                else:
                    self._promo_info_list.append(MPromoInfo.from_alipay_dict(i))
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.auto_delay_flag:
            if hasattr(self.auto_delay_flag, 'to_alipay_dict'):
                params['auto_delay_flag'] = self.auto_delay_flag.to_alipay_dict()
            else:
                params['auto_delay_flag'] = self.auto_delay_flag
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.operator_type:
            if hasattr(self.operator_type, 'to_alipay_dict'):
                params['operator_type'] = self.operator_type.to_alipay_dict()
            else:
                params['operator_type'] = self.operator_type
        if self.out_biz_type:
            if hasattr(self.out_biz_type, 'to_alipay_dict'):
                params['out_biz_type'] = self.out_biz_type.to_alipay_dict()
            else:
                params['out_biz_type'] = self.out_biz_type
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.promo_info_list:
            if isinstance(self.promo_info_list, list):
                for i in range(0, len(self.promo_info_list)):
                    element = self.promo_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.promo_info_list[i] = element.to_alipay_dict()
            if hasattr(self.promo_info_list, 'to_alipay_dict'):
                params['promo_info_list'] = self.promo_info_list.to_alipay_dict()
            else:
                params['promo_info_list'] = self.promo_info_list
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingCampaignMerchantActivityCreateModel()
        if 'auto_delay_flag' in d:
            o.auto_delay_flag = d['auto_delay_flag']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'desc' in d:
            o.desc = d['desc']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'name' in d:
            o.name = d['name']
        if 'operator' in d:
            o.operator = d['operator']
        if 'operator_type' in d:
            o.operator_type = d['operator_type']
        if 'out_biz_type' in d:
            o.out_biz_type = d['out_biz_type']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'promo_info_list' in d:
            o.promo_info_list = d['promo_info_list']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


