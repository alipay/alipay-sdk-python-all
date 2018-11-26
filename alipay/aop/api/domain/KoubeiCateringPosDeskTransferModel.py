#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeskAreaEntity import DeskAreaEntity
from alipay.aop.api.domain.SortDeskParam import SortDeskParam


class KoubeiCateringPosDeskTransferModel(object):

    def __init__(self):
        self._sort_area = None
        self._sort_desk = None

    @property
    def sort_area(self):
        return self._sort_area

    @sort_area.setter
    def sort_area(self, value):
        if isinstance(value, list):
            self._sort_area = list()
            for i in value:
                if isinstance(i, DeskAreaEntity):
                    self._sort_area.append(i)
                else:
                    self._sort_area.append(DeskAreaEntity.from_alipay_dict(i))
    @property
    def sort_desk(self):
        return self._sort_desk

    @sort_desk.setter
    def sort_desk(self, value):
        if isinstance(value, list):
            self._sort_desk = list()
            for i in value:
                if isinstance(i, SortDeskParam):
                    self._sort_desk.append(i)
                else:
                    self._sort_desk.append(SortDeskParam.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.sort_area:
            if isinstance(self.sort_area, list):
                for i in range(0, len(self.sort_area)):
                    element = self.sort_area[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sort_area[i] = element.to_alipay_dict()
            if hasattr(self.sort_area, 'to_alipay_dict'):
                params['sort_area'] = self.sort_area.to_alipay_dict()
            else:
                params['sort_area'] = self.sort_area
        if self.sort_desk:
            if isinstance(self.sort_desk, list):
                for i in range(0, len(self.sort_desk)):
                    element = self.sort_desk[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sort_desk[i] = element.to_alipay_dict()
            if hasattr(self.sort_desk, 'to_alipay_dict'):
                params['sort_desk'] = self.sort_desk.to_alipay_dict()
            else:
                params['sort_desk'] = self.sort_desk
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringPosDeskTransferModel()
        if 'sort_area' in d:
            o.sort_area = d['sort_area']
        if 'sort_desk' in d:
            o.sort_desk = d['sort_desk']
        return o


