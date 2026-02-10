#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShortPlaySourceMediaInfo import ShortPlaySourceMediaInfo


class AlipaySocialBaseLifecreationShortplayUploadModel(object):

    def __init__(self):
        self._public_id = None
        self._source_content = None
        self._source_media_infos = None
        self._source_title = None

    @property
    def public_id(self):
        return self._public_id

    @public_id.setter
    def public_id(self, value):
        self._public_id = value
    @property
    def source_content(self):
        return self._source_content

    @source_content.setter
    def source_content(self, value):
        self._source_content = value
    @property
    def source_media_infos(self):
        return self._source_media_infos

    @source_media_infos.setter
    def source_media_infos(self, value):
        if isinstance(value, list):
            self._source_media_infos = list()
            for i in value:
                if isinstance(i, ShortPlaySourceMediaInfo):
                    self._source_media_infos.append(i)
                else:
                    self._source_media_infos.append(ShortPlaySourceMediaInfo.from_alipay_dict(i))
    @property
    def source_title(self):
        return self._source_title

    @source_title.setter
    def source_title(self, value):
        self._source_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.public_id:
            if hasattr(self.public_id, 'to_alipay_dict'):
                params['public_id'] = self.public_id.to_alipay_dict()
            else:
                params['public_id'] = self.public_id
        if self.source_content:
            if hasattr(self.source_content, 'to_alipay_dict'):
                params['source_content'] = self.source_content.to_alipay_dict()
            else:
                params['source_content'] = self.source_content
        if self.source_media_infos:
            if isinstance(self.source_media_infos, list):
                for i in range(0, len(self.source_media_infos)):
                    element = self.source_media_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.source_media_infos[i] = element.to_alipay_dict()
            if hasattr(self.source_media_infos, 'to_alipay_dict'):
                params['source_media_infos'] = self.source_media_infos.to_alipay_dict()
            else:
                params['source_media_infos'] = self.source_media_infos
        if self.source_title:
            if hasattr(self.source_title, 'to_alipay_dict'):
                params['source_title'] = self.source_title.to_alipay_dict()
            else:
                params['source_title'] = self.source_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialBaseLifecreationShortplayUploadModel()
        if 'public_id' in d:
            o.public_id = d['public_id']
        if 'source_content' in d:
            o.source_content = d['source_content']
        if 'source_media_infos' in d:
            o.source_media_infos = d['source_media_infos']
        if 'source_title' in d:
            o.source_title = d['source_title']
        return o


