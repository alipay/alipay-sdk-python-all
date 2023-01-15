#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RcsmartSceneContentData import RcsmartSceneContentData


class RcsmartCommonApprovalReq(object):

    def __init__(self):
        self._biz_id = None
        self._ext_param = None
        self._parent_request_id = None
        self._request_id = None
        self._scene_content_data_list = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def parent_request_id(self):
        return self._parent_request_id

    @parent_request_id.setter
    def parent_request_id(self, value):
        self._parent_request_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def scene_content_data_list(self):
        return self._scene_content_data_list

    @scene_content_data_list.setter
    def scene_content_data_list(self, value):
        if isinstance(value, list):
            self._scene_content_data_list = list()
            for i in value:
                if isinstance(i, RcsmartSceneContentData):
                    self._scene_content_data_list.append(i)
                else:
                    self._scene_content_data_list.append(RcsmartSceneContentData.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.parent_request_id:
            if hasattr(self.parent_request_id, 'to_alipay_dict'):
                params['parent_request_id'] = self.parent_request_id.to_alipay_dict()
            else:
                params['parent_request_id'] = self.parent_request_id
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.scene_content_data_list:
            if isinstance(self.scene_content_data_list, list):
                for i in range(0, len(self.scene_content_data_list)):
                    element = self.scene_content_data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.scene_content_data_list[i] = element.to_alipay_dict()
            if hasattr(self.scene_content_data_list, 'to_alipay_dict'):
                params['scene_content_data_list'] = self.scene_content_data_list.to_alipay_dict()
            else:
                params['scene_content_data_list'] = self.scene_content_data_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RcsmartCommonApprovalReq()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'parent_request_id' in d:
            o.parent_request_id = d['parent_request_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'scene_content_data_list' in d:
            o.scene_content_data_list = d['scene_content_data_list']
        return o


