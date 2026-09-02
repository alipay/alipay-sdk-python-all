#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HyFileMeta import HyFileMeta
from alipay.aop.api.domain.HyFileMeta import HyFileMeta
from alipay.aop.api.domain.HyFileMeta import HyFileMeta


class AlipayCommerceMedicalHyFileBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHyFileBatchqueryResponse, self).__init__()
        self._file_list = None
        self._image_list = None
        self._video_list = None

    @property
    def file_list(self):
        return self._file_list

    @file_list.setter
    def file_list(self, value):
        if isinstance(value, list):
            self._file_list = list()
            for i in value:
                if isinstance(i, HyFileMeta):
                    self._file_list.append(i)
                else:
                    self._file_list.append(HyFileMeta.from_alipay_dict(i))
    @property
    def image_list(self):
        return self._image_list

    @image_list.setter
    def image_list(self, value):
        if isinstance(value, list):
            self._image_list = list()
            for i in value:
                if isinstance(i, HyFileMeta):
                    self._image_list.append(i)
                else:
                    self._image_list.append(HyFileMeta.from_alipay_dict(i))
    @property
    def video_list(self):
        return self._video_list

    @video_list.setter
    def video_list(self, value):
        if isinstance(value, list):
            self._video_list = list()
            for i in value:
                if isinstance(i, HyFileMeta):
                    self._video_list.append(i)
                else:
                    self._video_list.append(HyFileMeta.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHyFileBatchqueryResponse, self).parse_response_content(response_content)
        if 'file_list' in response:
            self.file_list = response['file_list']
        if 'image_list' in response:
            self.image_list = response['image_list']
        if 'video_list' in response:
            self.video_list = response['video_list']
