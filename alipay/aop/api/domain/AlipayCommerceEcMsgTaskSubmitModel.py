#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MsgSceneDTO import MsgSceneDTO


class AlipayCommerceEcMsgTaskSubmitModel(object):

    def __init__(self):
        self._enterprise_id = None
        self._msg_scene_list = None
        self._out_biz_no = None

    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def msg_scene_list(self):
        return self._msg_scene_list

    @msg_scene_list.setter
    def msg_scene_list(self, value):
        if isinstance(value, list):
            self._msg_scene_list = list()
            for i in value:
                if isinstance(i, MsgSceneDTO):
                    self._msg_scene_list.append(i)
                else:
                    self._msg_scene_list.append(MsgSceneDTO.from_alipay_dict(i))
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.msg_scene_list:
            if isinstance(self.msg_scene_list, list):
                for i in range(0, len(self.msg_scene_list)):
                    element = self.msg_scene_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.msg_scene_list[i] = element.to_alipay_dict()
            if hasattr(self.msg_scene_list, 'to_alipay_dict'):
                params['msg_scene_list'] = self.msg_scene_list.to_alipay_dict()
            else:
                params['msg_scene_list'] = self.msg_scene_list
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcMsgTaskSubmitModel()
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'msg_scene_list' in d:
            o.msg_scene_list = d['msg_scene_list']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


