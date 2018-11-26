#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExerciseRecordOpenModel import ExerciseRecordOpenModel


class KoubeiServindustryExerciseRecordSyncModel(object):

    def __init__(self):
        self._data_version = None
        self._fitness_id = None
        self._record_list = None
        self._shop_id = None

    @property
    def data_version(self):
        return self._data_version

    @data_version.setter
    def data_version(self, value):
        self._data_version = value
    @property
    def fitness_id(self):
        return self._fitness_id

    @fitness_id.setter
    def fitness_id(self, value):
        self._fitness_id = value
    @property
    def record_list(self):
        return self._record_list

    @record_list.setter
    def record_list(self, value):
        if isinstance(value, list):
            self._record_list = list()
            for i in value:
                if isinstance(i, ExerciseRecordOpenModel):
                    self._record_list.append(i)
                else:
                    self._record_list.append(ExerciseRecordOpenModel.from_alipay_dict(i))
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_version:
            if hasattr(self.data_version, 'to_alipay_dict'):
                params['data_version'] = self.data_version.to_alipay_dict()
            else:
                params['data_version'] = self.data_version
        if self.fitness_id:
            if hasattr(self.fitness_id, 'to_alipay_dict'):
                params['fitness_id'] = self.fitness_id.to_alipay_dict()
            else:
                params['fitness_id'] = self.fitness_id
        if self.record_list:
            if isinstance(self.record_list, list):
                for i in range(0, len(self.record_list)):
                    element = self.record_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.record_list[i] = element.to_alipay_dict()
            if hasattr(self.record_list, 'to_alipay_dict'):
                params['record_list'] = self.record_list.to_alipay_dict()
            else:
                params['record_list'] = self.record_list
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiServindustryExerciseRecordSyncModel()
        if 'data_version' in d:
            o.data_version = d['data_version']
        if 'fitness_id' in d:
            o.fitness_id = d['fitness_id']
        if 'record_list' in d:
            o.record_list = d['record_list']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


