#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.StageCateInfoVO import StageCateInfoVO


class StageGroupInfoVO(object):

    def __init__(self):
        self._group_name = None
        self._stage_cate_infos = None

    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def stage_cate_infos(self):
        return self._stage_cate_infos

    @stage_cate_infos.setter
    def stage_cate_infos(self, value):
        if isinstance(value, list):
            self._stage_cate_infos = list()
            for i in value:
                if isinstance(i, StageCateInfoVO):
                    self._stage_cate_infos.append(i)
                else:
                    self._stage_cate_infos.append(StageCateInfoVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        if self.stage_cate_infos:
            if isinstance(self.stage_cate_infos, list):
                for i in range(0, len(self.stage_cate_infos)):
                    element = self.stage_cate_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.stage_cate_infos[i] = element.to_alipay_dict()
            if hasattr(self.stage_cate_infos, 'to_alipay_dict'):
                params['stage_cate_infos'] = self.stage_cate_infos.to_alipay_dict()
            else:
                params['stage_cate_infos'] = self.stage_cate_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StageGroupInfoVO()
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'stage_cate_infos' in d:
            o.stage_cate_infos = d['stage_cate_infos']
        return o


