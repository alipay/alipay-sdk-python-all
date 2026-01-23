#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseObcinfraTasksealApplyModel(object):

    def __init__(self):
        self._deploy_cloud = None
        self._id = None
        self._x_boss_env = None

    @property
    def deploy_cloud(self):
        return self._deploy_cloud

    @deploy_cloud.setter
    def deploy_cloud(self, value):
        self._deploy_cloud = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def x_boss_env(self):
        return self._x_boss_env

    @x_boss_env.setter
    def x_boss_env(self, value):
        self._x_boss_env = value


    def to_alipay_dict(self):
        params = dict()
        if self.deploy_cloud:
            if hasattr(self.deploy_cloud, 'to_alipay_dict'):
                params['deploy_cloud'] = self.deploy_cloud.to_alipay_dict()
            else:
                params['deploy_cloud'] = self.deploy_cloud
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.x_boss_env:
            if hasattr(self.x_boss_env, 'to_alipay_dict'):
                params['x_boss_env'] = self.x_boss_env.to_alipay_dict()
            else:
                params['x_boss_env'] = self.x_boss_env
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObcinfraTasksealApplyModel()
        if 'deploy_cloud' in d:
            o.deploy_cloud = d['deploy_cloud']
        if 'id' in d:
            o.id = d['id']
        if 'x_boss_env' in d:
            o.x_boss_env = d['x_boss_env']
        return o


