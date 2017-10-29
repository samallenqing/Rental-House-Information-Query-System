package qq.model.service.impl;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import qq.model.entity.Ad;
import qq.model.repository.AdRepository;
import qq.model.service.AdService;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;


@Service
public class AdServiceImpl implements AdService {

    private AdRepository adRepository;


    @Autowired
    public AdServiceImpl(AdRepository adRepository){
        this.adRepository = adRepository;
    }


    @Override
    public List<Ad> findAdsByLocationOrZip(String zipCodeOrLocation) throws IOException {
        List<Ad> res = new ArrayList<>();
        List<Ad> res1 = adRepository.findAdsByLocationContains(zipCodeOrLocation);
        List<Ad> res2 = adRepository.findAdsByZipCode(zipCodeOrLocation);
        if(res1.size() != 0) {
            res.addAll(res1);
        }
        if (res2.size() != 0){
            res.addAll(res2);
        }
        if (res.size() != 0) {
            PrintWriter pw = new PrintWriter(new FileWriter("/Users/samqing/IdeaProjects/myRental/src/main/resources/static/where.js"));
            pw.write("myData = [");

            int count = 0;
            for (Ad sample : res){
                count++;
                String gps = sample.getGps();
                if (gps == null) continue;
                String detail = sample.getDescription();
                detail = detail.substring(0, detail.length() - 1);
                try {
                    pw.write("["+gps+",'"+detail+"']");
                } catch (Exception e){
                    throw e;
                }
                if (count == 10) break;
                pw.write(",\n");
            }
            pw.write("]");
            pw.close();
        }
        return res;
    }

}
