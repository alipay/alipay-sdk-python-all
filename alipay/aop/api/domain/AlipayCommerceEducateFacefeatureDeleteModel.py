#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ScenicFaceInfo import ScenicFaceInfo


class AlipayCommerceEducateFacefeatureDeleteModel(object):

    def __init__(self):
        self._biz_code = None
        self._biz_id = None
        self._ext_info = None
        self._group_id = None
        self._inst_id = None
        self._isv_name = None
        self._scenic_face_info = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def isv_name(self):
        return self._isv_name

    @isv_name.setter
    def isv_name(self, value):
        self._isv_name = value
    @property
    def scenic_face_info(self):
        return self._scenic_face_info

    @scenic_face_info.setter
    def scenic_face_info(self, value):
        if isinstance(value, list):
            self._scenic_face_info = list()
            for i in value:
                if isinstance(i, ScenicFaceInfo):
                    self._scenic_face_info.append(i)
                else:
                    self._scenic_face_info.append(ScenicFaceInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.isv_name:
            if hasattr(self.isv_name, 'to_alipay_dict'):
                params['isv_name'] = self.isv_name.to_alipay_dict()
            else:
                params['isv_name'] = self.isv_name
        if self.scenic_face_info:
            if isinstance(self.scenic_face_info, list):
                for i in range(0, len(self.scenic_face_info)):
                    element = self.scenic_face_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.scenic_face_info[i] = element.to_alipay_dict()
            if hasattr(self.scenic_face_info, 'to_alipay_dict'):
                params['scenic_face_info'] = self.scenic_face_info.to_alipay_dict()
            else:
                params['scenic_face_info'] = self.scenic_face_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateFacefeatureDeleteModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'isv_name' in d:
            o.isv_name = d['isv_name']
        if 'scenic_face_info' in d:
            o.scenic_face_info = d['scenic_face_info']
        return o


