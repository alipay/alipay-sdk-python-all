#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GoodInfo import GoodInfo


class AlipayMsaasMediarecogMmportalCvgooodsonlinelistSyncModel(object):

    def __init__(self):
        self._biz_id = None
        self._device_id = None
        self._effect_transaction_ids = None
        self._external_info = None
        self._goods_infos = None
        self._goods_list = None
        self._isv_pid = None
        self._single_pad_door_pos = None
        self._submit_time = None
        self._template_id = None
        self._type = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def effect_transaction_ids(self):
        return self._effect_transaction_ids

    @effect_transaction_ids.setter
    def effect_transaction_ids(self, value):
        if isinstance(value, list):
            self._effect_transaction_ids = list()
            for i in value:
                self._effect_transaction_ids.append(i)
    @property
    def external_info(self):
        return self._external_info

    @external_info.setter
    def external_info(self, value):
        self._external_info = value
    @property
    def goods_infos(self):
        return self._goods_infos

    @goods_infos.setter
    def goods_infos(self, value):
        if isinstance(value, list):
            self._goods_infos = list()
            for i in value:
                if isinstance(i, GoodInfo):
                    self._goods_infos.append(i)
                else:
                    self._goods_infos.append(GoodInfo.from_alipay_dict(i))
    @property
    def goods_list(self):
        return self._goods_list

    @goods_list.setter
    def goods_list(self, value):
        if isinstance(value, list):
            self._goods_list = list()
            for i in value:
                self._goods_list.append(i)
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def single_pad_door_pos(self):
        return self._single_pad_door_pos

    @single_pad_door_pos.setter
    def single_pad_door_pos(self, value):
        self._single_pad_door_pos = value
    @property
    def submit_time(self):
        return self._submit_time

    @submit_time.setter
    def submit_time(self, value):
        self._submit_time = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.effect_transaction_ids:
            if isinstance(self.effect_transaction_ids, list):
                for i in range(0, len(self.effect_transaction_ids)):
                    element = self.effect_transaction_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.effect_transaction_ids[i] = element.to_alipay_dict()
            if hasattr(self.effect_transaction_ids, 'to_alipay_dict'):
                params['effect_transaction_ids'] = self.effect_transaction_ids.to_alipay_dict()
            else:
                params['effect_transaction_ids'] = self.effect_transaction_ids
        if self.external_info:
            if hasattr(self.external_info, 'to_alipay_dict'):
                params['external_info'] = self.external_info.to_alipay_dict()
            else:
                params['external_info'] = self.external_info
        if self.goods_infos:
            if isinstance(self.goods_infos, list):
                for i in range(0, len(self.goods_infos)):
                    element = self.goods_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_infos[i] = element.to_alipay_dict()
            if hasattr(self.goods_infos, 'to_alipay_dict'):
                params['goods_infos'] = self.goods_infos.to_alipay_dict()
            else:
                params['goods_infos'] = self.goods_infos
        if self.goods_list:
            if isinstance(self.goods_list, list):
                for i in range(0, len(self.goods_list)):
                    element = self.goods_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_list[i] = element.to_alipay_dict()
            if hasattr(self.goods_list, 'to_alipay_dict'):
                params['goods_list'] = self.goods_list.to_alipay_dict()
            else:
                params['goods_list'] = self.goods_list
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.single_pad_door_pos:
            if hasattr(self.single_pad_door_pos, 'to_alipay_dict'):
                params['single_pad_door_pos'] = self.single_pad_door_pos.to_alipay_dict()
            else:
                params['single_pad_door_pos'] = self.single_pad_door_pos
        if self.submit_time:
            if hasattr(self.submit_time, 'to_alipay_dict'):
                params['submit_time'] = self.submit_time.to_alipay_dict()
            else:
                params['submit_time'] = self.submit_time
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogMmportalCvgooodsonlinelistSyncModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'effect_transaction_ids' in d:
            o.effect_transaction_ids = d['effect_transaction_ids']
        if 'external_info' in d:
            o.external_info = d['external_info']
        if 'goods_infos' in d:
            o.goods_infos = d['goods_infos']
        if 'goods_list' in d:
            o.goods_list = d['goods_list']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'single_pad_door_pos' in d:
            o.single_pad_door_pos = d['single_pad_door_pos']
        if 'submit_time' in d:
            o.submit_time = d['submit_time']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'type' in d:
            o.type = d['type']
        return o


