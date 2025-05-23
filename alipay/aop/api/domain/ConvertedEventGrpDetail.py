#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConvertedEventDetail import ConvertedEventDetail


class ConvertedEventGrpDetail(object):

    def __init__(self):
        self._converted_event_detail_list = None
        self._converted_event_grp = None
        self._converted_event_grp_name = None

    @property
    def converted_event_detail_list(self):
        return self._converted_event_detail_list

    @converted_event_detail_list.setter
    def converted_event_detail_list(self, value):
        if isinstance(value, list):
            self._converted_event_detail_list = list()
            for i in value:
                if isinstance(i, ConvertedEventDetail):
                    self._converted_event_detail_list.append(i)
                else:
                    self._converted_event_detail_list.append(ConvertedEventDetail.from_alipay_dict(i))
    @property
    def converted_event_grp(self):
        return self._converted_event_grp

    @converted_event_grp.setter
    def converted_event_grp(self, value):
        self._converted_event_grp = value
    @property
    def converted_event_grp_name(self):
        return self._converted_event_grp_name

    @converted_event_grp_name.setter
    def converted_event_grp_name(self, value):
        self._converted_event_grp_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.converted_event_detail_list:
            if isinstance(self.converted_event_detail_list, list):
                for i in range(0, len(self.converted_event_detail_list)):
                    element = self.converted_event_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.converted_event_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.converted_event_detail_list, 'to_alipay_dict'):
                params['converted_event_detail_list'] = self.converted_event_detail_list.to_alipay_dict()
            else:
                params['converted_event_detail_list'] = self.converted_event_detail_list
        if self.converted_event_grp:
            if hasattr(self.converted_event_grp, 'to_alipay_dict'):
                params['converted_event_grp'] = self.converted_event_grp.to_alipay_dict()
            else:
                params['converted_event_grp'] = self.converted_event_grp
        if self.converted_event_grp_name:
            if hasattr(self.converted_event_grp_name, 'to_alipay_dict'):
                params['converted_event_grp_name'] = self.converted_event_grp_name.to_alipay_dict()
            else:
                params['converted_event_grp_name'] = self.converted_event_grp_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConvertedEventGrpDetail()
        if 'converted_event_detail_list' in d:
            o.converted_event_detail_list = d['converted_event_detail_list']
        if 'converted_event_grp' in d:
            o.converted_event_grp = d['converted_event_grp']
        if 'converted_event_grp_name' in d:
            o.converted_event_grp_name = d['converted_event_grp_name']
        return o


