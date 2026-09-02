#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsPetOrgprofileverifyIdentifyModel(object):

    def __init__(self):
        self._out_biz_no = None
        self._pet_face_url = None
        self._pet_id = None

    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def pet_face_url(self):
        return self._pet_face_url

    @pet_face_url.setter
    def pet_face_url(self, value):
        self._pet_face_url = value
    @property
    def pet_id(self):
        return self._pet_id

    @pet_id.setter
    def pet_id(self, value):
        self._pet_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.pet_face_url:
            if hasattr(self.pet_face_url, 'to_alipay_dict'):
                params['pet_face_url'] = self.pet_face_url.to_alipay_dict()
            else:
                params['pet_face_url'] = self.pet_face_url
        if self.pet_id:
            if hasattr(self.pet_id, 'to_alipay_dict'):
                params['pet_id'] = self.pet_id.to_alipay_dict()
            else:
                params['pet_id'] = self.pet_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsPetOrgprofileverifyIdentifyModel()
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'pet_face_url' in d:
            o.pet_face_url = d['pet_face_url']
        if 'pet_id' in d:
            o.pet_id = d['pet_id']
        return o


