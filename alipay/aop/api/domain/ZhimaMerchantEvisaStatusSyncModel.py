#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApprovedInfo import ApprovedInfo
from alipay.aop.api.domain.VerifiedInfo import VerifiedInfo


class ZhimaMerchantEvisaStatusSyncModel(object):

    def __init__(self):
        self._action_type = None
        self._approved_infos = None
        self._biz_time = None
        self._out_biz_no = None
        self._scene_type = None
        self._verified_infos = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def approved_infos(self):
        return self._approved_infos

    @approved_infos.setter
    def approved_infos(self, value):
        if isinstance(value, list):
            self._approved_infos = list()
            for i in value:
                if isinstance(i, ApprovedInfo):
                    self._approved_infos.append(i)
                else:
                    self._approved_infos.append(ApprovedInfo.from_alipay_dict(i))
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value
    @property
    def verified_infos(self):
        return self._verified_infos

    @verified_infos.setter
    def verified_infos(self, value):
        if isinstance(value, list):
            self._verified_infos = list()
            for i in value:
                if isinstance(i, VerifiedInfo):
                    self._verified_infos.append(i)
                else:
                    self._verified_infos.append(VerifiedInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.approved_infos:
            if isinstance(self.approved_infos, list):
                for i in range(0, len(self.approved_infos)):
                    element = self.approved_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.approved_infos[i] = element.to_alipay_dict()
            if hasattr(self.approved_infos, 'to_alipay_dict'):
                params['approved_infos'] = self.approved_infos.to_alipay_dict()
            else:
                params['approved_infos'] = self.approved_infos
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        if self.verified_infos:
            if isinstance(self.verified_infos, list):
                for i in range(0, len(self.verified_infos)):
                    element = self.verified_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.verified_infos[i] = element.to_alipay_dict()
            if hasattr(self.verified_infos, 'to_alipay_dict'):
                params['verified_infos'] = self.verified_infos.to_alipay_dict()
            else:
                params['verified_infos'] = self.verified_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaMerchantEvisaStatusSyncModel()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'approved_infos' in d:
            o.approved_infos = d['approved_infos']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        if 'verified_infos' in d:
            o.verified_infos = d['verified_infos']
        return o


