#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LifeServiceRoomInfo import LifeServiceRoomInfo
from alipay.aop.api.domain.LifeServiceShopInfo import LifeServiceShopInfo


class LifeServiceBookInfo(object):

    def __init__(self):
        self._book_id = None
        self._room_infos = None
        self._shop_info = None

    @property
    def book_id(self):
        return self._book_id

    @book_id.setter
    def book_id(self, value):
        self._book_id = value
    @property
    def room_infos(self):
        return self._room_infos

    @room_infos.setter
    def room_infos(self, value):
        if isinstance(value, list):
            self._room_infos = list()
            for i in value:
                if isinstance(i, LifeServiceRoomInfo):
                    self._room_infos.append(i)
                else:
                    self._room_infos.append(LifeServiceRoomInfo.from_alipay_dict(i))
    @property
    def shop_info(self):
        return self._shop_info

    @shop_info.setter
    def shop_info(self, value):
        if isinstance(value, LifeServiceShopInfo):
            self._shop_info = value
        else:
            self._shop_info = LifeServiceShopInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.book_id:
            if hasattr(self.book_id, 'to_alipay_dict'):
                params['book_id'] = self.book_id.to_alipay_dict()
            else:
                params['book_id'] = self.book_id
        if self.room_infos:
            if isinstance(self.room_infos, list):
                for i in range(0, len(self.room_infos)):
                    element = self.room_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.room_infos[i] = element.to_alipay_dict()
            if hasattr(self.room_infos, 'to_alipay_dict'):
                params['room_infos'] = self.room_infos.to_alipay_dict()
            else:
                params['room_infos'] = self.room_infos
        if self.shop_info:
            if hasattr(self.shop_info, 'to_alipay_dict'):
                params['shop_info'] = self.shop_info.to_alipay_dict()
            else:
                params['shop_info'] = self.shop_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LifeServiceBookInfo()
        if 'book_id' in d:
            o.book_id = d['book_id']
        if 'room_infos' in d:
            o.room_infos = d['room_infos']
        if 'shop_info' in d:
            o.shop_info = d['shop_info']
        return o


