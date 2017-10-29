package qq.model.rest;


import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import qq.model.entity.Ad;
import qq.model.service.AdService;

import java.io.IOException;
import java.util.List;

@RestController
@RequestMapping(value = "/api")
@Slf4j
public class AdRestController {

    private AdService adService;

    @Autowired
    public AdRestController(AdService adService){
        this.adService = adService;
    }


    @RequestMapping(value = "ads/{zipCode}", method = RequestMethod.GET)
    public List<Ad> findByZipCode(@PathVariable String zipCode) throws IOException {
        return adService.findAdsByLocationOrZip(zipCode);
    }
}

