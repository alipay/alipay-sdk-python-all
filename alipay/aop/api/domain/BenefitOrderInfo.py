#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BenefitRewardInfo import BenefitRewardInfo
from alipay.aop.api.domain.BenefitRightOrderInfo import BenefitRightOrderInfo


class BenefitOrderInfo(object):

    def __init__(self):
        self._end_time = None
        self._open_id = None
        self._order_id = None
        self._out_biz_no = None
        self._out_biz_type = None
        self._reward_info = None
        self._right_order_info_list = None
        self._scene_code = None
        self._start_time = None
        self._status = None
        self._sub_scene_code = None
        self._template_code = None
        self._user_id = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_biz_type(self):
        return self._out_biz_type

    @out_biz_type.setter
    def out_biz_type(self, value):
        self._out_biz_type = value
    @property
    def reward_info(self):
        return self._reward_info

    @reward_info.setter
    def reward_info(self, value):
        if isinstance(value, BenefitRewardInfo):
            self._reward_info = value
        else:
            self._reward_info = BenefitRewardInfo.from_alipay_dict(value)
    @property
    def right_order_info_list(self):
        return self._right_order_info_list

    @right_order_info_list.setter
    def right_order_info_list(self, value):
        if isinstance(value, list):
            self._right_order_info_list = list()
            for i in value:
                if isinstance(i, BenefitRightOrderInfo):
                    self._right_order_info_list.append(i)
                else:
                    self._right_order_info_list.append(BenefitRightOrderInfo.from_alipay_dict(i))
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
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
    @property
    def sub_scene_code(self):
        return self._sub_scene_code

    @sub_scene_code.setter
    def sub_scene_code(self, value):
        self._sub_scene_code = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_biz_type:
            if hasattr(self.out_biz_type, 'to_alipay_dict'):
                params['out_biz_type'] = self.out_biz_type.to_alipay_dict()
            else:
                params['out_biz_type'] = self.out_biz_type
        if self.reward_info:
            if hasattr(self.reward_info, 'to_alipay_dict'):
                params['reward_info'] = self.reward_info.to_alipay_dict()
            else:
                params['reward_info'] = self.reward_info
        if self.right_order_info_list:
            if isinstance(self.right_order_info_list, list):
                for i in range(0, len(self.right_order_info_list)):
                    element = self.right_order_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.right_order_info_list[i] = element.to_alipay_dict()
            if hasattr(self.right_order_info_list, 'to_alipay_dict'):
                params['right_order_info_list'] = self.right_order_info_list.to_alipay_dict()
            else:
                params['right_order_info_list'] = self.right_order_info_list
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
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
        if self.sub_scene_code:
            if hasattr(self.sub_scene_code, 'to_alipay_dict'):
                params['sub_scene_code'] = self.sub_scene_code.to_alipay_dict()
            else:
                params['sub_scene_code'] = self.sub_scene_code
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
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
        o = BenefitOrderInfo()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_biz_type' in d:
            o.out_biz_type = d['out_biz_type']
        if 'reward_info' in d:
            o.reward_info = d['reward_info']
        if 'right_order_info_list' in d:
            o.right_order_info_list = d['right_order_info_list']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        if 'sub_scene_code' in d:
            o.sub_scene_code = d['sub_scene_code']
        if 'template_code' in d:
            o.template_code = d['template_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


