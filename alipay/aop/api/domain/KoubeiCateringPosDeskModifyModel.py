#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeskEntity import DeskEntity


class KoubeiCateringPosDeskModifyModel(object):

    def __init__(self):
        self._pos_desk = None

    @property
    def pos_desk(self):
        return self._pos_desk

    @pos_desk.setter
    def pos_desk(self, value):
        if isinstance(value, DeskEntity):
            self._pos_desk = value
        else:
            self._pos_desk = DeskEntity.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.pos_desk:
            if hasattr(self.pos_desk, 'to_alipay_dict'):
                params['pos_desk'] = self.pos_desk.to_alipay_dict()
            else:
                params['pos_desk'] = self.pos_desk
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringPosDeskModifyModel()
        if 'pos_desk' in d:
            o.pos_desk = d['pos_desk']
        return o


