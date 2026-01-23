#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AnchorInstance import AnchorInstance
from alipay.aop.api.domain.QualInstanceDTO import QualInstanceDTO


class Qualification(object):

    def __init__(self):
        self._anchor_instance = None
        self._apply_status = None
        self._apply_status_desc = None
        self._asset_info = None
        self._qual_id = None
        self._qualification_instance = None
        self._template_id = None

    @property
    def anchor_instance(self):
        return self._anchor_instance

    @anchor_instance.setter
    def anchor_instance(self, value):
        if isinstance(value, AnchorInstance):
            self._anchor_instance = value
        else:
            self._anchor_instance = AnchorInstance.from_alipay_dict(value)
    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value
    @property
    def apply_status_desc(self):
        return self._apply_status_desc

    @apply_status_desc.setter
    def apply_status_desc(self, value):
        self._apply_status_desc = value
    @property
    def asset_info(self):
        return self._asset_info

    @asset_info.setter
    def asset_info(self, value):
        self._asset_info = value
    @property
    def qual_id(self):
        return self._qual_id

    @qual_id.setter
    def qual_id(self, value):
        self._qual_id = value
    @property
    def qualification_instance(self):
        return self._qualification_instance

    @qualification_instance.setter
    def qualification_instance(self, value):
        if isinstance(value, QualInstanceDTO):
            self._qualification_instance = value
        else:
            self._qualification_instance = QualInstanceDTO.from_alipay_dict(value)
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.anchor_instance:
            if hasattr(self.anchor_instance, 'to_alipay_dict'):
                params['anchor_instance'] = self.anchor_instance.to_alipay_dict()
            else:
                params['anchor_instance'] = self.anchor_instance
        if self.apply_status:
            if hasattr(self.apply_status, 'to_alipay_dict'):
                params['apply_status'] = self.apply_status.to_alipay_dict()
            else:
                params['apply_status'] = self.apply_status
        if self.apply_status_desc:
            if hasattr(self.apply_status_desc, 'to_alipay_dict'):
                params['apply_status_desc'] = self.apply_status_desc.to_alipay_dict()
            else:
                params['apply_status_desc'] = self.apply_status_desc
        if self.asset_info:
            if hasattr(self.asset_info, 'to_alipay_dict'):
                params['asset_info'] = self.asset_info.to_alipay_dict()
            else:
                params['asset_info'] = self.asset_info
        if self.qual_id:
            if hasattr(self.qual_id, 'to_alipay_dict'):
                params['qual_id'] = self.qual_id.to_alipay_dict()
            else:
                params['qual_id'] = self.qual_id
        if self.qualification_instance:
            if hasattr(self.qualification_instance, 'to_alipay_dict'):
                params['qualification_instance'] = self.qualification_instance.to_alipay_dict()
            else:
                params['qualification_instance'] = self.qualification_instance
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Qualification()
        if 'anchor_instance' in d:
            o.anchor_instance = d['anchor_instance']
        if 'apply_status' in d:
            o.apply_status = d['apply_status']
        if 'apply_status_desc' in d:
            o.apply_status_desc = d['apply_status_desc']
        if 'asset_info' in d:
            o.asset_info = d['asset_info']
        if 'qual_id' in d:
            o.qual_id = d['qual_id']
        if 'qualification_instance' in d:
            o.qualification_instance = d['qualification_instance']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


