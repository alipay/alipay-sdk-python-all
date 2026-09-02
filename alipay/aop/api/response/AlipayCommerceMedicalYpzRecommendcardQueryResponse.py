#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.YpzAfuDownloadCardOne import YpzAfuDownloadCardOne
from alipay.aop.api.domain.YpzCloudDispenseMedicineCardOne import YpzCloudDispenseMedicineCardOne
from alipay.aop.api.domain.YpzCloudDispenseMedicineHomeCardOne import YpzCloudDispenseMedicineHomeCardOne
from alipay.aop.api.domain.YpzDoctorAgentCardOne import YpzDoctorAgentCardOne
from alipay.aop.api.domain.YpzMedAccompanyCardOne import YpzMedAccompanyCardOne
from alipay.aop.api.domain.YpzNpsCardOne import YpzNpsCardOne
from alipay.aop.api.domain.YpzOfflineQrCodeCardOne import YpzOfflineQrCodeCardOne
from alipay.aop.api.domain.YpzQaCardOne import YpzQaCardOne


class AlipayCommerceMedicalYpzRecommendcardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalYpzRecommendcardQueryResponse, self).__init__()
        self._afu_download_card = None
        self._cloud_dispense_medicine_card = None
        self._cloud_dispense_medicine_home_card = None
        self._delivery_type = None
        self._doctor_agent_card = None
        self._med_accompany_card = None
        self._nps_card = None
        self._offline_qr_code_card = None
        self._qa_card = None

    @property
    def afu_download_card(self):
        return self._afu_download_card

    @afu_download_card.setter
    def afu_download_card(self, value):
        if isinstance(value, YpzAfuDownloadCardOne):
            self._afu_download_card = value
        else:
            self._afu_download_card = YpzAfuDownloadCardOne.from_alipay_dict(value)
    @property
    def cloud_dispense_medicine_card(self):
        return self._cloud_dispense_medicine_card

    @cloud_dispense_medicine_card.setter
    def cloud_dispense_medicine_card(self, value):
        if isinstance(value, YpzCloudDispenseMedicineCardOne):
            self._cloud_dispense_medicine_card = value
        else:
            self._cloud_dispense_medicine_card = YpzCloudDispenseMedicineCardOne.from_alipay_dict(value)
    @property
    def cloud_dispense_medicine_home_card(self):
        return self._cloud_dispense_medicine_home_card

    @cloud_dispense_medicine_home_card.setter
    def cloud_dispense_medicine_home_card(self, value):
        if isinstance(value, list):
            self._cloud_dispense_medicine_home_card = list()
            for i in value:
                if isinstance(i, YpzCloudDispenseMedicineHomeCardOne):
                    self._cloud_dispense_medicine_home_card.append(i)
                else:
                    self._cloud_dispense_medicine_home_card.append(YpzCloudDispenseMedicineHomeCardOne.from_alipay_dict(i))
    @property
    def delivery_type(self):
        return self._delivery_type

    @delivery_type.setter
    def delivery_type(self, value):
        self._delivery_type = value
    @property
    def doctor_agent_card(self):
        return self._doctor_agent_card

    @doctor_agent_card.setter
    def doctor_agent_card(self, value):
        if isinstance(value, YpzDoctorAgentCardOne):
            self._doctor_agent_card = value
        else:
            self._doctor_agent_card = YpzDoctorAgentCardOne.from_alipay_dict(value)
    @property
    def med_accompany_card(self):
        return self._med_accompany_card

    @med_accompany_card.setter
    def med_accompany_card(self, value):
        if isinstance(value, YpzMedAccompanyCardOne):
            self._med_accompany_card = value
        else:
            self._med_accompany_card = YpzMedAccompanyCardOne.from_alipay_dict(value)
    @property
    def nps_card(self):
        return self._nps_card

    @nps_card.setter
    def nps_card(self, value):
        if isinstance(value, YpzNpsCardOne):
            self._nps_card = value
        else:
            self._nps_card = YpzNpsCardOne.from_alipay_dict(value)
    @property
    def offline_qr_code_card(self):
        return self._offline_qr_code_card

    @offline_qr_code_card.setter
    def offline_qr_code_card(self, value):
        if isinstance(value, YpzOfflineQrCodeCardOne):
            self._offline_qr_code_card = value
        else:
            self._offline_qr_code_card = YpzOfflineQrCodeCardOne.from_alipay_dict(value)
    @property
    def qa_card(self):
        return self._qa_card

    @qa_card.setter
    def qa_card(self, value):
        if isinstance(value, YpzQaCardOne):
            self._qa_card = value
        else:
            self._qa_card = YpzQaCardOne.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalYpzRecommendcardQueryResponse, self).parse_response_content(response_content)
        if 'afu_download_card' in response:
            self.afu_download_card = response['afu_download_card']
        if 'cloud_dispense_medicine_card' in response:
            self.cloud_dispense_medicine_card = response['cloud_dispense_medicine_card']
        if 'cloud_dispense_medicine_home_card' in response:
            self.cloud_dispense_medicine_home_card = response['cloud_dispense_medicine_home_card']
        if 'delivery_type' in response:
            self.delivery_type = response['delivery_type']
        if 'doctor_agent_card' in response:
            self.doctor_agent_card = response['doctor_agent_card']
        if 'med_accompany_card' in response:
            self.med_accompany_card = response['med_accompany_card']
        if 'nps_card' in response:
            self.nps_card = response['nps_card']
        if 'offline_qr_code_card' in response:
            self.offline_qr_code_card = response['offline_qr_code_card']
        if 'qa_card' in response:
            self.qa_card = response['qa_card']
