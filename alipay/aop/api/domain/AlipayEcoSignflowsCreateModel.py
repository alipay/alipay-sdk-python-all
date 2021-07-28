#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Attachment import Attachment
from alipay.aop.api.domain.ConfigInfoBean import ConfigInfoBean
from alipay.aop.api.domain.TemplateInfoBean import TemplateInfoBean


class AlipayEcoSignflowsCreateModel(object):

    def __init__(self):
        self._attachments = None
        self._business_scene = None
        self._config_info = None
        self._template_infos = None

    @property
    def attachments(self):
        return self._attachments

    @attachments.setter
    def attachments(self, value):
        if isinstance(value, Attachment):
            self._attachments = value
        else:
            self._attachments = Attachment.from_alipay_dict(value)
    @property
    def business_scene(self):
        return self._business_scene

    @business_scene.setter
    def business_scene(self, value):
        self._business_scene = value
    @property
    def config_info(self):
        return self._config_info

    @config_info.setter
    def config_info(self, value):
        if isinstance(value, ConfigInfoBean):
            self._config_info = value
        else:
            self._config_info = ConfigInfoBean.from_alipay_dict(value)
    @property
    def template_infos(self):
        return self._template_infos

    @template_infos.setter
    def template_infos(self, value):
        if isinstance(value, TemplateInfoBean):
            self._template_infos = value
        else:
            self._template_infos = TemplateInfoBean.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.attachments:
            if hasattr(self.attachments, 'to_alipay_dict'):
                params['attachments'] = self.attachments.to_alipay_dict()
            else:
                params['attachments'] = self.attachments
        if self.business_scene:
            if hasattr(self.business_scene, 'to_alipay_dict'):
                params['business_scene'] = self.business_scene.to_alipay_dict()
            else:
                params['business_scene'] = self.business_scene
        if self.config_info:
            if hasattr(self.config_info, 'to_alipay_dict'):
                params['config_info'] = self.config_info.to_alipay_dict()
            else:
                params['config_info'] = self.config_info
        if self.template_infos:
            if hasattr(self.template_infos, 'to_alipay_dict'):
                params['template_infos'] = self.template_infos.to_alipay_dict()
            else:
                params['template_infos'] = self.template_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoSignflowsCreateModel()
        if 'attachments' in d:
            o.attachments = d['attachments']
        if 'business_scene' in d:
            o.business_scene = d['business_scene']
        if 'config_info' in d:
            o.config_info = d['config_info']
        if 'template_infos' in d:
            o.template_infos = d['template_infos']
        return o


