#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Attachment import Attachment
from alipay.aop.api.domain.ConfigInfo import ConfigInfo
from alipay.aop.api.domain.TemplateInfo import TemplateInfo


class AlipayEcoSignFlowCreateModel(object):

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
        if isinstance(value, list):
            self._attachments = list()
            for i in value:
                if isinstance(i, Attachment):
                    self._attachments.append(i)
                else:
                    self._attachments.append(Attachment.from_alipay_dict(i))
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
        if isinstance(value, ConfigInfo):
            self._config_info = value
        else:
            self._config_info = ConfigInfo.from_alipay_dict(value)
    @property
    def template_infos(self):
        return self._template_infos

    @template_infos.setter
    def template_infos(self, value):
        if isinstance(value, list):
            self._template_infos = list()
            for i in value:
                if isinstance(i, TemplateInfo):
                    self._template_infos.append(i)
                else:
                    self._template_infos.append(TemplateInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.attachments:
            if isinstance(self.attachments, list):
                for i in range(0, len(self.attachments)):
                    element = self.attachments[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attachments[i] = element.to_alipay_dict()
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
            if isinstance(self.template_infos, list):
                for i in range(0, len(self.template_infos)):
                    element = self.template_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.template_infos[i] = element.to_alipay_dict()
            if hasattr(self.template_infos, 'to_alipay_dict'):
                params['template_infos'] = self.template_infos.to_alipay_dict()
            else:
                params['template_infos'] = self.template_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoSignFlowCreateModel()
        if 'attachments' in d:
            o.attachments = d['attachments']
        if 'business_scene' in d:
            o.business_scene = d['business_scene']
        if 'config_info' in d:
            o.config_info = d['config_info']
        if 'template_infos' in d:
            o.template_infos = d['template_infos']
        return o


