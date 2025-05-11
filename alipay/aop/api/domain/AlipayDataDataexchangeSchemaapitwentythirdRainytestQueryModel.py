#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyComplexTypesRefWeakFifth import RainyComplexTypesRefWeakFifth
from alipay.aop.api.domain.RainyComplexTypesTheThirteen import RainyComplexTypesTheThirteen
from alipay.aop.api.domain.RainyComplexTypesTheFourteen import RainyComplexTypesTheFourteen
from alipay.aop.api.domain.RainyComplexTypesTheFourteenOne import RainyComplexTypesTheFourteenOne


class AlipayDataDataexchangeSchemaapitwentythirdRainytestQueryModel(object):

    def __init__(self):
        self._demo = None
        self._demo_ref = None
        self._demo_strong_ref = None
        self._demo_vv_ref = None
        self._demo_wink_ref = None

    @property
    def demo(self):
        return self._demo

    @demo.setter
    def demo(self, value):
        self._demo = value
    @property
    def demo_ref(self):
        return self._demo_ref

    @demo_ref.setter
    def demo_ref(self, value):
        if isinstance(value, RainyComplexTypesRefWeakFifth):
            self._demo_ref = value
        else:
            self._demo_ref = RainyComplexTypesRefWeakFifth.from_alipay_dict(value)
    @property
    def demo_strong_ref(self):
        return self._demo_strong_ref

    @demo_strong_ref.setter
    def demo_strong_ref(self, value):
        if isinstance(value, RainyComplexTypesTheThirteen):
            self._demo_strong_ref = value
        else:
            self._demo_strong_ref = RainyComplexTypesTheThirteen.from_alipay_dict(value)
    @property
    def demo_vv_ref(self):
        return self._demo_vv_ref

    @demo_vv_ref.setter
    def demo_vv_ref(self, value):
        if isinstance(value, RainyComplexTypesTheFourteen):
            self._demo_vv_ref = value
        else:
            self._demo_vv_ref = RainyComplexTypesTheFourteen.from_alipay_dict(value)
    @property
    def demo_wink_ref(self):
        return self._demo_wink_ref

    @demo_wink_ref.setter
    def demo_wink_ref(self, value):
        if isinstance(value, RainyComplexTypesTheFourteenOne):
            self._demo_wink_ref = value
        else:
            self._demo_wink_ref = RainyComplexTypesTheFourteenOne.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.demo:
            if hasattr(self.demo, 'to_alipay_dict'):
                params['demo'] = self.demo.to_alipay_dict()
            else:
                params['demo'] = self.demo
        if self.demo_ref:
            if hasattr(self.demo_ref, 'to_alipay_dict'):
                params['demo_ref'] = self.demo_ref.to_alipay_dict()
            else:
                params['demo_ref'] = self.demo_ref
        if self.demo_strong_ref:
            if hasattr(self.demo_strong_ref, 'to_alipay_dict'):
                params['demo_strong_ref'] = self.demo_strong_ref.to_alipay_dict()
            else:
                params['demo_strong_ref'] = self.demo_strong_ref
        if self.demo_vv_ref:
            if hasattr(self.demo_vv_ref, 'to_alipay_dict'):
                params['demo_vv_ref'] = self.demo_vv_ref.to_alipay_dict()
            else:
                params['demo_vv_ref'] = self.demo_vv_ref
        if self.demo_wink_ref:
            if hasattr(self.demo_wink_ref, 'to_alipay_dict'):
                params['demo_wink_ref'] = self.demo_wink_ref.to_alipay_dict()
            else:
                params['demo_wink_ref'] = self.demo_wink_ref
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataexchangeSchemaapitwentythirdRainytestQueryModel()
        if 'demo' in d:
            o.demo = d['demo']
        if 'demo_ref' in d:
            o.demo_ref = d['demo_ref']
        if 'demo_strong_ref' in d:
            o.demo_strong_ref = d['demo_strong_ref']
        if 'demo_vv_ref' in d:
            o.demo_vv_ref = d['demo_vv_ref']
        if 'demo_wink_ref' in d:
            o.demo_wink_ref = d['demo_wink_ref']
        return o


