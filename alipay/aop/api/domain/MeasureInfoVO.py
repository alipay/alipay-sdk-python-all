#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MeasureUnitInfoVO import MeasureUnitInfoVO
from alipay.aop.api.domain.MeasureUnitInfoVO import MeasureUnitInfoVO


class MeasureInfoVO(object):

    def __init__(self):
        self._percent_unit = None
        self._template_id = None
        self._unit_info = None

    @property
    def percent_unit(self):
        return self._percent_unit

    @percent_unit.setter
    def percent_unit(self, value):
        if isinstance(value, MeasureUnitInfoVO):
            self._percent_unit = value
        else:
            self._percent_unit = MeasureUnitInfoVO.from_alipay_dict(value)
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def unit_info(self):
        return self._unit_info

    @unit_info.setter
    def unit_info(self, value):
        if isinstance(value, MeasureUnitInfoVO):
            self._unit_info = value
        else:
            self._unit_info = MeasureUnitInfoVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.percent_unit:
            if hasattr(self.percent_unit, 'to_alipay_dict'):
                params['percent_unit'] = self.percent_unit.to_alipay_dict()
            else:
                params['percent_unit'] = self.percent_unit
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.unit_info:
            if hasattr(self.unit_info, 'to_alipay_dict'):
                params['unit_info'] = self.unit_info.to_alipay_dict()
            else:
                params['unit_info'] = self.unit_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MeasureInfoVO()
        if 'percent_unit' in d:
            o.percent_unit = d['percent_unit']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'unit_info' in d:
            o.unit_info = d['unit_info']
        return o


