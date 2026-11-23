#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpUboInfo(object):

    def __init__(self):
        self._bene_share_ratio = None
        self._control_way = None
        self._identify_criteria = None
        self._identify_way = None
        self._layer = None
        self._position_type = None
        self._record_type = None
        self._ubo_end_date = None
        self._ubo_ext = None
        self._ubo_form_date = None
        self._ubo_name = None
        self._vote_right_ratio = None

    @property
    def bene_share_ratio(self):
        return self._bene_share_ratio

    @bene_share_ratio.setter
    def bene_share_ratio(self, value):
        self._bene_share_ratio = value
    @property
    def control_way(self):
        return self._control_way

    @control_way.setter
    def control_way(self, value):
        self._control_way = value
    @property
    def identify_criteria(self):
        return self._identify_criteria

    @identify_criteria.setter
    def identify_criteria(self, value):
        self._identify_criteria = value
    @property
    def identify_way(self):
        return self._identify_way

    @identify_way.setter
    def identify_way(self, value):
        self._identify_way = value
    @property
    def layer(self):
        return self._layer

    @layer.setter
    def layer(self, value):
        self._layer = value
    @property
    def position_type(self):
        return self._position_type

    @position_type.setter
    def position_type(self, value):
        self._position_type = value
    @property
    def record_type(self):
        return self._record_type

    @record_type.setter
    def record_type(self, value):
        self._record_type = value
    @property
    def ubo_end_date(self):
        return self._ubo_end_date

    @ubo_end_date.setter
    def ubo_end_date(self, value):
        self._ubo_end_date = value
    @property
    def ubo_ext(self):
        return self._ubo_ext

    @ubo_ext.setter
    def ubo_ext(self, value):
        self._ubo_ext = value
    @property
    def ubo_form_date(self):
        return self._ubo_form_date

    @ubo_form_date.setter
    def ubo_form_date(self, value):
        self._ubo_form_date = value
    @property
    def ubo_name(self):
        return self._ubo_name

    @ubo_name.setter
    def ubo_name(self, value):
        self._ubo_name = value
    @property
    def vote_right_ratio(self):
        return self._vote_right_ratio

    @vote_right_ratio.setter
    def vote_right_ratio(self, value):
        self._vote_right_ratio = value


    def to_alipay_dict(self):
        params = dict()
        if self.bene_share_ratio:
            if hasattr(self.bene_share_ratio, 'to_alipay_dict'):
                params['bene_share_ratio'] = self.bene_share_ratio.to_alipay_dict()
            else:
                params['bene_share_ratio'] = self.bene_share_ratio
        if self.control_way:
            if hasattr(self.control_way, 'to_alipay_dict'):
                params['control_way'] = self.control_way.to_alipay_dict()
            else:
                params['control_way'] = self.control_way
        if self.identify_criteria:
            if hasattr(self.identify_criteria, 'to_alipay_dict'):
                params['identify_criteria'] = self.identify_criteria.to_alipay_dict()
            else:
                params['identify_criteria'] = self.identify_criteria
        if self.identify_way:
            if hasattr(self.identify_way, 'to_alipay_dict'):
                params['identify_way'] = self.identify_way.to_alipay_dict()
            else:
                params['identify_way'] = self.identify_way
        if self.layer:
            if hasattr(self.layer, 'to_alipay_dict'):
                params['layer'] = self.layer.to_alipay_dict()
            else:
                params['layer'] = self.layer
        if self.position_type:
            if hasattr(self.position_type, 'to_alipay_dict'):
                params['position_type'] = self.position_type.to_alipay_dict()
            else:
                params['position_type'] = self.position_type
        if self.record_type:
            if hasattr(self.record_type, 'to_alipay_dict'):
                params['record_type'] = self.record_type.to_alipay_dict()
            else:
                params['record_type'] = self.record_type
        if self.ubo_end_date:
            if hasattr(self.ubo_end_date, 'to_alipay_dict'):
                params['ubo_end_date'] = self.ubo_end_date.to_alipay_dict()
            else:
                params['ubo_end_date'] = self.ubo_end_date
        if self.ubo_ext:
            if hasattr(self.ubo_ext, 'to_alipay_dict'):
                params['ubo_ext'] = self.ubo_ext.to_alipay_dict()
            else:
                params['ubo_ext'] = self.ubo_ext
        if self.ubo_form_date:
            if hasattr(self.ubo_form_date, 'to_alipay_dict'):
                params['ubo_form_date'] = self.ubo_form_date.to_alipay_dict()
            else:
                params['ubo_form_date'] = self.ubo_form_date
        if self.ubo_name:
            if hasattr(self.ubo_name, 'to_alipay_dict'):
                params['ubo_name'] = self.ubo_name.to_alipay_dict()
            else:
                params['ubo_name'] = self.ubo_name
        if self.vote_right_ratio:
            if hasattr(self.vote_right_ratio, 'to_alipay_dict'):
                params['vote_right_ratio'] = self.vote_right_ratio.to_alipay_dict()
            else:
                params['vote_right_ratio'] = self.vote_right_ratio
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpUboInfo()
        if 'bene_share_ratio' in d:
            o.bene_share_ratio = d['bene_share_ratio']
        if 'control_way' in d:
            o.control_way = d['control_way']
        if 'identify_criteria' in d:
            o.identify_criteria = d['identify_criteria']
        if 'identify_way' in d:
            o.identify_way = d['identify_way']
        if 'layer' in d:
            o.layer = d['layer']
        if 'position_type' in d:
            o.position_type = d['position_type']
        if 'record_type' in d:
            o.record_type = d['record_type']
        if 'ubo_end_date' in d:
            o.ubo_end_date = d['ubo_end_date']
        if 'ubo_ext' in d:
            o.ubo_ext = d['ubo_ext']
        if 'ubo_form_date' in d:
            o.ubo_form_date = d['ubo_form_date']
        if 'ubo_name' in d:
            o.ubo_name = d['ubo_name']
        if 'vote_right_ratio' in d:
            o.vote_right_ratio = d['vote_right_ratio']
        return o


